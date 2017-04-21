''' This file is where we define all routes and site-related logic'''
from flask import Flask, render_template, url_for, request, redirect
from SearchForm import SearchForm
from BookParser import BookParser

app = Flask(__name__, static_url_path='/static')

bp = BookParser()

def no_dupes(list1, list2):
    result = []
    list1.extend(list2)
    for book in list1:
        if book not in result:
            result.append(book)
    return result

#Routes
@app.route('/', methods=['GET', 'POST'])
def home():
    form = SearchForm(request.form)
    if request.method == 'POST' and form.validate():
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

        return render_template('main.html', form=form, results=results)

    return render_template('main.html', form=form)

#Route for book details page
@app.route('/book/<isbn>', methods=['GET'])
def book_details(isbn):
    form = SearchForm(request.form)
    book = bp.search_by_isbn(isbn)
    return render_template('book.html', book=book[0], form=form)

#Route for about page
@app.route('/about', methods=['GET'])
def about():
    #Just return static template
    form = SearchForm(request.form)
    return render_template('about.html', form=form)

#Route for FAQ page
@app.route('/about/faq', methods=['GET'])
def faq():
    #Just return static template
    form = SearchForm(request.form)
    return render_template('faq.html', form=form)

#Route for FAQ page
@app.route('/about/contact', methods=['GET'])
def contact():
    #Just return static template
    form = SearchForm(request.form)
    return render_template('contact.html', form=form)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
