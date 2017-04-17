''' This file is where we define all routes and site-related logic'''
from flask import Flask, render_template, url_for, request, redirect
from BookParser import BookParser

app = Flask(__name__, static_url_path='/static')

#Routes

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        #this method is called when the '/' endpoint receives a POST request
        results = []
        form = request.form
        #TODO: Add search for other keywords
        bp = BookParser()
        if form['ISBN'] is not None:
            results = bp.search_by_isbn(form['ISBN'])
        return render_template('main.html', results=results)

    return render_template('main.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
