''' This file is where we define all routes and site-related logic'''
from flask import Flask, render_template, url_for, request, redirect, session, flash
from Forms import SearchForm, BookTypeForm, ShoppingCartForm, CheckoutForm
from flask_mail import Mail, Message
from BookParser import BookParser
from ShoppingCart import ShoppingCart
from InvoiceFactory import InvoiceFactory

app = Flask(__name__)
mail = Mail(app)
app.secret_key = '(-)<(Yo*u(*&)+-los&t*+th(e//+_ga$me)'

app.config.update(
        MAIL_SERVER='smtp.gmail.com',
        MAIL_PORT='465',
        MAIL_USE_SSL=True,
        MAIL_USERNAME='mailer.ksubooks@gmail.com',
        MAIL_PASSWORD='kennesaw420*'
)

mail = Mail(app)

bp = BookParser()
sc = ShoppingCart()
inv_factory = InvoiceFactory()

#Routes
@app.route('/', methods=['GET', 'POST'])
def home():
    if 'cart' in session:
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
            if int(book_to_add[bp.STOCK_NEW]) < 1:
                #Can't add to cart
                if request.form['sender'] is not None:
                    if request.form['sender'] == 'book':
                        book = bp.search_by_isbn(form.isbn.data)
                        return render_template('book.html', book=book[0], bookform=form, form=search_form, cart_count=cart_count, error="Out of stock!")
                return ('', 204)
            else:
                price = book_to_add[bp.PRICE_NEW]
        if form.types.data == 'Rent':
            if int(book_to_add[bp.STOCK_RENT]) < 1:
                #Can't add to cart
                if request.form['sender'] is not None:
                    if request.form['sender'] == 'book':
                        book = bp.search_by_isbn(form.isbn.data)
                        return render_template('book.html', book=book[0], bookform=form, form=search_form, cart_count=cart_count, error="Out of stock!")
                return ('', 204)
            else:
                price = book_to_add[bp.PRICE_RENT]
        if form.types.data == 'Used':
            if int(book_to_add[bp.STOCK_USED]) < 1:
                #Can't add to cart
                if request.form['sender'] is not None:
                    if request.form['sender'] == 'book':
                        book = bp.search_by_isbn(form.isbn.data)
                        return render_template('book.html', book=book[0], bookform=form, form=search_form, cart_count=cart_count, error="Out of stock!")
                return ('', 204)
            else:
                price = book_to_add[bp.PRICE_USED]
        if form.types.data == 'E-book':
            if int(book_to_add[bp.STOCK_EBOOK]) < 1:
                #Can't add to cart
                if request.form['sender'] is not None:
                    if request.form['sender'] == 'book':
                        book = bp.search_by_isbn(form.isbn.data)
                        return render_template('book.html', book=book[0], bookform=form, form=search_form, cart_count=cart_count, error="Out of stock!")
                if request.form['search'] is not None:
                    print request.form['search']
                return ('', 204)
            else:
                price = book_to_add[bp.PRICE_EBOOK]

        if session['cart'] is None:
            session['cart'] = []
        cart = session['cart']
        cart.append({'book': book_to_add, 'type': form.types.data, 'count': 1, 'price': price})
        session['cart'] = cart
        cart_count = len(session['cart'])

        return ('', 204)
    else:
        for field, errors in form.errors.items():
            for error in errors:
                print u"Error in the %s field - %s" % (getattr(form, field).label.text, error)
        return ('', 204)
        #render_template('main.html', form=search_form, results=results, bookform=form, cart_count=cart_count)

#Endpoint for editing cart items
@app.route('/cart/edit', methods=['POST'])
def rem_from_cart():
    form = ShoppingCartForm(request.form)
    search_form = SearchForm(request.form)
    cartform = ShoppingCartForm(request.form)

    if form.validate():
        #Request is for qty edit
        cart = sc.edit_item_qty(form.isbn.data, form.qty.data)
        session['cart'] = cart

        subtotal = sc.get_cart_subtotal()
        tax = subtotal *.07
        return render_template('shoppingcart.html', cart=cart, form=search_form, cartform=cartform, cart_count=sc.get_cart_size(), subtotal=round(subtotal, 2), tax=round(tax, 2))
    else:
        if request.form['isbn'] is not None:
            #Request is for item removal
            form = request.form
            if form['isbn'] is not None:
                cart = sc.delete_item(form['isbn'])
                session['cart'] = cart

            subtotal = sc.get_cart_subtotal()
            tax = subtotal *.07
            return render_template('shoppingcart.html', cart=session['cart'], form=search_form, cartform=cartform, cart_count=sc.get_cart_size(), subtotal=round(subtotal, 2), tax=round(tax, 2))

#Route for shopping cart
@app.route('/cart', methods=['GET'])
def show_cart():
    cart_count = sc.get_cart_size()
    subtotal = sc.get_cart_subtotal()
    sub_ship = subtotal + 14.99
    tax = sub_ship * .07
    cartform = ShoppingCartForm(request.form)
    form = SearchForm(request.form)
    return render_template('shoppingcart.html', cart=session['cart'], form=form, cartform=cartform, cart_count=cart_count, subtotal=subtotal, tax=round(tax, 2))

#Route for checkout page
@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    if request.method == 'POST':
        checkout_form = CheckoutForm(request.form)
        #Form hell!!
        if checkout_form.validate():
            '''Get invoice dictionary'''
            invoice_dict = inv_factory.checkout_to_invoice(checkout_form)
            invoice = invoice_dict
            #Validate login data
            if invoice_dict['type'] == 'fa':
                #Make sure user exists, and has enough money
                users = inv_factory.get_users()
                for user in users:
                    if checkout_form.fa_login.data == user[2]:
                        if checkout_form.fa_password.data == user[3]:
                            st = sc.get_cart_subtotal()
                            st_sh = st + 14.99
                            tax = st_sh * .07
                            total = st_sh+14.99+tax
                            if float(user[4]) > total:
                                '''Write to invoice file'''
                                inv_factory.write_to_file(invoice_dict)
                                search_form = SearchForm(request.form)
                                st = sc.get_cart_subtotal()
                                st_sh = st + 14.99
                                tax = st_sh * .07

                                list_string = ''
                                for entry in sc.get_cart():
                                    book = entry['book']
                                    type = entry['type']
                                    count = entry['count']
                                    if type == 'E-book':
                                        string_to_add = "%s x %s (%s)\nDownload: https://ebooksrus.com/%s/download.php" % (book[1], str(count), type, book[0])
                                    else:
                                        string_to_add = "%s x %s (%s)\n" % (book[1], str(count), type)
                                    list_string += string_to_add
                                    bp.update_stock(book[0], type, count)

                                email = checkout_form.email.data
                                name = invoice['ship_name']
                                addr = invoice['ship_addr']
                                city = invoice['ship_city']
                                state = invoice['ship_state']
                                zip = invoice['ship_zip']
                                addr_string = "%s\n%s\n%s, %s %s" % (name, addr, city, state, zip)
                                #Send receipt as email
                                message = "%s,\nHere is your receipt for your recent purchase on the KSU online bookstore.\n\nBooks purchased: \n%s\n\nShipped to:\n%s" % (name, str(list_string), addr_string)
                                msg = Message(
                                    'Your KSU Books Receipt',
                                    sender='KSUBooksMailer',
                                    recipients=[email])
                                msg.body = message
                                mail.send(msg)

                                return render_template('receipt.html', invoice=invoice_dict, cart=session['cart'], form=search_form, cart_count=sc.get_cart_size(), subtotal=sc.get_cart_subtotal(), tax=round(tax, 2))
                            else:
                                errors= ['Insufficient funds!']
                                search_form = SearchForm(request.form)
                                st = sc.get_cart_subtotal()
                                st_sh = st + 14.99
                                tax = st_sh * .07
                                payment_type = request.args.get('payment')
                                billing_form = CheckoutForm(request.form)
                                return render_template('checkout.html', payment=payment_type, cart=session['cart'], errors=errors, form=search_form, billing_form=billing_form, cart_count=sc.get_cart_size(), subtotal=sc.get_cart_subtotal(), tax=round(tax, 2))
                        else:
                            errors= ['Incorrect login!']
                            search_form = SearchForm(request.form)
                            st = sc.get_cart_subtotal()
                            st_sh = st + 14.99
                            tax = st_sh * .07
                            payment_type = request.args.get('payment')
                            billing_form = CheckoutForm(request.form)
                            return render_template('checkout.html', payment=payment_type, cart=session['cart'], errors=errors, form=search_form, billing_form=billing_form, cart_count=sc.get_cart_size(), subtotal=sc.get_cart_subtotal(), tax=round(tax, 2))

            elif invoice_dict['type'] == 'pp':
                '''Email is validated by wtforms'''
                if checkout_form.pp_password.data == '123456789':
                    '''Write to invoice file'''
                    inv_factory.write_to_file(invoice_dict)
                    search_form = SearchForm(request.form)
                    st = sc.get_cart_subtotal()
                    st_sh = st + 14.99
                    tax = st_sh * .07

                    list_string = ''
                    for entry in sc.get_cart():
                        book = entry['book']
                        type = entry['type']
                        count = entry['count']
                        if type == 'E-book':
                            string_to_add = "%s x %s (%s)\nDownload: https://ebooksrus.com/%s/download.php" % (book[1], str(count), type, book[0])
                        else:
                            string_to_add = "%s x %s (%s)\n" % (book[1], str(count), type)
                        list_string += string_to_add
                        bp.update_stock(book[0], type, count)

                    email = checkout_form.email.data
                    name = invoice['ship_name']
                    addr = invoice['ship_addr']
                    city = invoice['ship_city']
                    state = invoice['ship_state']
                    zip = invoice['ship_zip']
                    addr_string = "%s\n%s\n%s, %s %s" % (name, addr, city, state, zip)
                    #Send receipt as email
                    message = "%s,\nHere is your receipt for your recent purchase on the KSU online bookstore.\n\nBooks purchased: \n%s\n\nShipped to:\n%s" % (name, str(list_string), addr_string)
                    msg = Message(
                        'Your KSU Books Receipt',
                        sender='KSUBooksMailer',
                        recipients=[email])
                    msg.body = message
                    mail.send(msg)

                    return render_template('receipt.html', invoice=invoice_dict, cart=session['cart'], form=search_form, cart_count=sc.get_cart_size(), subtotal=sc.get_cart_subtotal(), tax=round(tax, 2))
                else:
                    errors= ['Incorrect login!']
                    search_form = SearchForm(request.form)
                    st = sc.get_cart_subtotal()
                    st_sh = st + 14.99
                    tax = st_sh * .07
                    payment_type = request.args.get('payment')
                    billing_form = CheckoutForm(request.form)
                    return render_template('checkout.html', payment=payment_type, cart=session['cart'], errors=errors, form=search_form, billing_form=billing_form, cart_count=sc.get_cart_size(), subtotal=sc.get_cart_subtotal(), tax=round(tax, 2))
            elif invoice_dict['type'] == 'cc':
                '''cc data is verified by wtforms validators'''
                if checkout_form.cvv.data is not None:
                    '''Write to invoice file'''
                    inv_factory.write_to_file(invoice_dict)
                    search_form = SearchForm(request.form)
                    st = sc.get_cart_subtotal()
                    st_sh = st + 14.99
                    tax = st_sh * .07
                    list_string = ''
                    for entry in sc.get_cart():
                        book = entry['book']
                        type = entry['type']
                        count = entry['count']
                        if type == 'E-book':
                            string_to_add = "%s x %s (%s)\nDownload: https://ebooksrus.com/%s/download.php" % (book[1], str(count), type, book[0])
                        else:
                            string_to_add = "%s x %s (%s)\n" % (book[1], str(count), type)
                        list_string += string_to_add
                        bp.update_stock(book[0], type, count)

                    email = checkout_form.email.data
                    name = invoice['ship_name']
                    addr = invoice['ship_addr']
                    city = invoice['ship_city']
                    state = invoice['ship_state']
                    zip = invoice['ship_zip']
                    addr_string = "%s\n%s\n%s, %s %s" % (name, addr, city, state, zip)
                    #Send receipt as email
                    message = "%s,\nHere is your receipt for your recent purchase on the KSU online bookstore.\n\nBooks purchased: \n%s\n\nShipped to:\n%s" % (name, str(list_string), addr_string)
                    msg = Message(
                        'Your KSU Books Receipt',
                        sender='KSUBooksMailer',
                        recipients=[email])
                    msg.body = message
                    mail.send(msg)
                    return render_template('receipt.html', invoice=invoice_dict, cart=session['cart'], form=search_form, cart_count=sc.get_cart_size(), subtotal=sc.get_cart_subtotal(), tax=round(tax, 2))
                else:
                    errors= ['Card declined- check CVV!']
                    search_form = SearchForm(request.form)
                    st = sc.get_cart_subtotal()
                    st_sh = st + 14.99
                    tax = st_sh * .07
                    payment_type = request.args.get('payment')
                    billing_form = CheckoutForm(request.form)
                    return render_template('checkout.html', payment=payment_type, cart=session['cart'], errors=errors, form=search_form, billing_form=billing_form, cart_count=sc.get_cart_size(), subtotal=sc.get_cart_subtotal(), tax=round(tax, 2))

        else:
            form_errors = []
            for field, errors in checkout_form.errors.items():
                for error in errors:
                    form_errors.append(u"Error: %s - %s" % (getattr(checkout_form, field).label.text, error))

            search_form = SearchForm(request.form)
            st = sc.get_cart_subtotal()
            st_sh = st + 14.99
            tax = st_sh * .07

            payment_type = request.args.get('payment')
            billing_form = CheckoutForm(request.form)
            return render_template('checkout.html', payment=payment_type, cart=session['cart'], errors=form_errors, form=search_form, billing_form=billing_form, cart_count=sc.get_cart_size(), subtotal=sc.get_cart_subtotal(), tax=round(tax, 2))
    else:
        search_form = SearchForm(request.form)
        st = sc.get_cart_subtotal()
        st_sh = st + 14.99
        tax = st_sh * .07

        payment_type = request.args.get('payment')
        billing_form = CheckoutForm(request.form)

        return render_template('checkout.html', payment=payment_type, cart=session['cart'], form=search_form, billing_form=billing_form, cart_count=sc.get_cart_size(), subtotal=sc.get_cart_subtotal(), tax=round(tax, 2))

#Sends email to provided address
def send_email(msg, adr):
    msg = Message(
        'Your KSU Books Receipt',
        sender='KSUBooksMailer',
        recipients=[adr])
    msg.body = msg
    mail.send(msg)

#Route for book details page
@app.route('/book/<isbn>', methods=['GET'])
def book_details(isbn):
    cart_count = len(session['cart'])
    form = SearchForm(request.form)
    book_form = BookTypeForm(request.form)
    book = bp.search_by_isbn(isbn)
    return render_template('book.html', book=book[0], bookform=book_form, form=form, cart_count=cart_count)

#Route for about page
@app.route('/about', methods=['GET'])
def about():
    #Just return static template
    cart_count = len(session['cart'])
    form = SearchForm(request.form)
    return render_template('about.html', form=form, cart_count=cart_count)

#Route for FAQ page
@app.route('/faq', methods=['GET'])
def faq():
    #Just return static template
    cart_count = len(session['cart'])
    form = SearchForm(request.form)
    return render_template('faq.html', form=form, cart_count=cart_count)

#Route for FAQ page
@app.route('/contact', methods=['GET'])
def contact():
    #Just return static template
    cart_count = len(session['cart'])
    form = SearchForm(request.form)
    return render_template('contact.html', form=form, cart_count=cart_count)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
