<<<<<<< HEAD
# swe-final-2k17
Repo for best team 2k17
=======
# PYHTON BITCHES!!!!!!!!  
No time for VS BS amirite?!?

# TDD
TDD: Test Driven Development

What's TDD?? Google it!  

In short:  
Write tests BEFORE coding!

# How do I write tests???

Basically you'll write a test method before each method you write. The method will run the implementation and confirm the output.  

# Example!!

Let's say we're writing a method called `csv_to_dict_list()` in the class `BookParser`  
The method is expected to return a list of books.  
In order to test this, we'll create a seperate Test file for the `BookParser` class.  

So inside of `BookParserTest.py` we'll reference the class and make a method called `should_ret_list()`  

It'll look something like this:  
```python
from BookParser import BookParser
bp = BookParser()

def should_ret_list():
    result = 'should_ret_list: '
    book_list = bp.csv_to_dict_list()
    if len(book_list) > 0:
        print result +'PASS'
    else:
        print result +'FAIL'
```

In order to run the tests, we should create a new method called `run_all_tests` and call each test method  
So in this case, it would look like:  

```python
def run_all_tests():
    should_ret_list()
```

And lastly, we need to tell python to actually run that method! When you run a script from python, it doesn't know what method to call.  

We tell it to run `run_all_tests()` like so:

```python
if __name__ == "__main__":
    run_all_tests()
```

Once that is at the end of the test script, we can run it from the command like like so:  
`python BookParserTest.py`

# I wrote the tests, now what??

Well now, you write the method!

A python crash course:  
We'll continue with the `BookParser` example:  

First, make a python file called `BookParser.py`  
Next, you have to declare the class. The class name, obviously, should match the name of the file.  

So in this case:  
`BookParser.py`  
```python
class BookParser:
    #Indent after the class declaration!
```

To define functions, you:  
`BookParser.py`  

```python
class BookParser:
    val = 0 # an instance variable
    # This is a method:
    def this_is_a_method(self):
        #Make sure to indent after the method dec.
        print 'Fuck'
        #If the method returns a value, just return it.
        #You don't need to define return types anywhere!
        return 'Fuck'
```

Methods within a class need to take `self` as an argument. This is not reflected in any method calls, though.

# Running the site
The framework we're using is a 'microframework' for building web apps with python.  
It's called `Flask`. To run the site, simply start the `app.py` file:  
`python app.py`  

If you get an error saying something along the lines of: "Module 'Flask' not found", you'll need to install flask!  
Lucky for you, an idiot could do it!  

When you installed python on your computer it came with a nifty program called `pip`.  
`pip` is a package manager for python. You can install flask by opening your admin command prompt or PowerShell and running:  
`pip install flask`  

If you don't have pip installed, you'll need to reinstall python. Woops.

Anyway once the site is running, open up a web browser and head to: `http://localhost:5000/`  
There, you'll be greeted with the site's index page. Check the command prompt for debugger output!
