''' This file is where we define all routes and site-related logic'''
from flask import Flask, render_template, url_for, request, redirect
from SearchForm import SearchForm
from BookParser import BookParser

app = Flask(__name__, static_url_path='/static')

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
        print 'Hello form!'
        results = []
        bp = BookParser()

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


        return render_template('main.html', form=form, results=results)

    return render_template('main.html', form=form)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
