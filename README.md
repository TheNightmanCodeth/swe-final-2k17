## Yo

# TDD
TDD: Test Driven Development

What's TDD?? Google it!
In short:
Write tests BEFORE code!

# How do I write tests???

EZPZ, Create a //Test.py file for the module you're writing
create a method for the feature you're testing.  
For example, if you're writing the function for turning the books file into a list,
you would make a file called BookParser.py and BookParserTest.py.  
Inside the BookParserTest.py, you'll create a BookParser object.  
Then, make a function called `should_ret_list`, since you're testing that the  
BookParser will return a list.  
Think, what should the module I'm testing do??  

In this case, it should return a list. EZ.

Make a variable to store the list, and make sure it's larger than 0!!  
`if len(list) > 0:`  
print to console the name of the method, and PASS.

If that doesn't make any sense just check out my actual tests and hopefully  
you'll understand the actual code.

# I wrote the tests, now what??

Well now, you write the method!
