''' This file is where we define all routes and site-related logic'''
from flask import Flask, render_template, url_for, request, redirect
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
    if request.method == 'POST':
        #this method is called when the '/' endpoint receives a POST request
        results = []
        form = request.form
        #TODO: Add search for other keywords
        bp = BookParser()
        if request.form.get('ISBN', None) is not None:
            isbn = request.form.get('ISBN', None)
            results_isbn = bp.search_by_isbn(isbn)
            if results_isbn is not -1:
                for book in results_isbn:
                    if book not in results:
                        results.append(book)
        if request.form.get('prof', None) is not None:
            print 'form'
            prof = request.form.get('prof', None)
            results_prof = bp.search_by_prof(prof)
            if results_prof is not -1:
                for book in results_prof:
                    if book not in results:
                        results.append(book)

        return render_template('main.html', results=results)

    return render_template('main.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
