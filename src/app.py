''' This file is where we define all routes and site-related logic'''
from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static')

#Routes

@app.route('/')
def home():
    #this method is called when the '/' endpoint receives a GET request
    return render_template('main.html')
