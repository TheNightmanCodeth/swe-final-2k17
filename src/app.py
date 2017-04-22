''' This file is where we define all routes and site-related logic'''
from flask import Flask, render_template, url_for, request, redirect, session, flash
from Forms import SearchForm, BookTypeForm, ShoppingCartForm
from BookParser import BookParser

app = Flask(__name__)
app.secret_key = '(-)<(Yo*u(*&)+-los&t*+th(e//+_ga$me)'

bp = BookParser()

#Routes
@app.route('/', methods=['GET', 'POST'])
def home():
    if session['cart'] is not None:
        cart_count = len(session['cart'])
    else:
        session['cart'] = []
        cart_count = len(session['cart'])
    form = SearchForm(request.form)
    bookform = BookTypeForm(request.form)
    if request.method == 'POST':
        if form.validate():
            #this method is called when the '/' endpoint receives a POST request
            results = []
            if form.isbn.data is not None:
                isbn = form.isbn.data
                results_isbn = bp.search_by_isbn(isbn)
                if results_isbn is not -1:
                    for book in results_isbn:
                        if book not in results:
                            results.append(book)
            if form.prof.data is not None:
                prof = form.prof.data
                results_prof = bp.search_by_prof(prof)
                if results_prof is not -1:
                    for book in results_prof:
                        if book not in results:
                            results.append(book)
            if form.title.data is not None:
                title = form.title.data
                results_title = bp.search_by_title(title)
                if results_title is not -1:
                    for book in results_title:
                        if book not in results:
                            results.append(book)
            if form.classs.data is not None:
                classs = form.classs.data
                results_class = bp.search_by_class(classs)
                if results_class is not -1:
                    for book in results_class:
                        if book not in results:
                            results.append(book)
            if form.keyword.data is not None:
                keyword = form.keyword.data
                results_kw = bp.search_by_desc(keyword)
                if results_kw is not -1:
                    for book in results_kw:
                        if book not in results:
                            results.append(book)
            if form.author.data is not None:
                author = form.author.data
                results_author = bp.search_by_author(author)
                if results_author is not -1:
                    for book in results_author:
                        if book not in results:
                            results.append(book)
            return render_template('main.html', form=form, results=results, bookform=bookform, cart_count=cart_count)
    return render_template('main.html', form=form, bookform=bookform, cart_count=cart_count)

#Endpoint for adding item to cart
@app.route('/cart/add', methods=['POST'])
def add_to_cart():
    cart_count = len(session['cart'])
    search_form = SearchForm(request.form)
    form = BookTypeForm(request.form)
    if request.method == 'POST' and form.validate():
        #Grab search results passed from hidded form data
        results = form.search.data
        #Add ISBN and type to cart
        book_to_add = bp.search_by_isbn(form.isbn.data)[0]
        if form.types.data == 'New':
            if book_to_add[bp.STOCK_NEW] < 1:
                #Can't add to cart
                flash("Can't add that type!")
                return ('', 204)
            else:
                price = book_to_add[bp.PRICE_NEW]
        if form.types.data == 'Rent':
            if book_to_add[bp.STOCK_RENT] < 1:
                #Can't add to cart
                flash("Can't add that type!")
                return ('', 204)
            else:
                price = book_to_add[bp.PRICE_RENT]
        if form.types.data == 'Used':
            if book_to_add[bp.STOCK_USED] < 1:
                #Can't add to cart
                flash("Can't add that type!")
                return ('', 204)
            else:
                price = book_to_add[bp.PRICE_USED]
        if form.types.data == 'E-book':
            if book_to_add[bp.STOCK_EBOOK] < 1:
                #Can't add to cart
                flash("Can't add that type!")
                return ('', 204)
            else:
                price = book_to_add[bp.PRICE_EBOOK]

        if session['cart'] is None:
            session['cart'] = []
        cart = session['cart']
        cart.append({'book': book_to_add, 'type': form.types.data, 'count': 2, 'price': price})
        session['cart'] = cart
        cart_count = len(session['cart'])
        return ('', 204)
        #render_template('main.html', form=search_form, results=results, bookform=form, cart_count=cart_count)

#Endpoint for editing cart items
@app.route('/cart/edit', methods=['POST'])
def rem_from_cart():
    form = ShoppingCartForm(request.form)
    search_form = SearchForm(request.form)
    cartform = ShoppingCartForm(request.form)
    if form.validate():
        new_qty = int(form.qty.data)
        cart = session['cart']
        for entry in cart:
            isbn = entry['book'][0]
            if form.isbn.data == isbn:
                if form.qty.data == '0':
                    cart = delete_item(isbn)
                else:
                    entry['count'] = form.qty.data

        session['cart'] = cart
        return render_template('shoppingcart.html', cart=cart, form=search_form, cartform=cartform, cart_count=len(session['cart']))
    else:
        if request.form['isbn'] is not None:
            search_form = SearchForm(request.form)
            cartform = ShoppingCartForm(request.form)
            form = request.form
            if form['isbn'] is not None:
                cart = delete_item(form['isbn'])
                session['cart'] = cart
                cart_count = len(session['cart'])
            return render_template('shoppingcart.html', cart=cart, form=search_form, cartform=cartform, cart_count=cart_count)

def delete_item(form_isbn):
    index = 0
    cart = session['cart']
    for entry in cart:
        isbn = entry['book'][0]
        if form_isbn == isbn:
            del cart[index]
        index += 1
    return cart

#Route for shopping cart
@app.route('/cart', methods=['GET'])
def show_cart():
    cart_count = len(session['cart'])
    cart = session['cart']
    cartform = ShoppingCartForm(request.form)
    form = SearchForm(request.form)
    return render_template('shoppingcart.html', cart=cart, form=form, cartform=cartform, cart_count=cart_count)

#Route for book details page
@app.route('/book/<isbn>', methods=['GET'])
def book_details(isbn):
    cart_count = len(session['cart'])
    form = SearchForm(request.form)
    book = bp.search_by_isbn(isbn)
    return render_template('book.html', book=book[0], form=form, cart_count=cart_count)

#Route for about page
@app.route('/about', methods=['GET'])
def about():
    #Just return static template
    cart_count = len(session['cart'])
    form = SearchForm(request.form)
    return render_template('about.html', form=form, cart_count=cart_count)

#Route for FAQ page
@app.route('/about/faq', methods=['GET'])
def faq():
    #Just return static template
    cart_count = len(session['cart'])
    form = SearchForm(request.form)
    return render_template('faq.html', form=form, cart_count=cart_count)

#Route for FAQ page
@app.route('/about/contact', methods=['GET'])
def contact():
    #Just return static template
    cart_count = len(session['cart'])
    form = SearchForm(request.form)
    return render_template('contact.html', form=form, cart_count=cart_count)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
