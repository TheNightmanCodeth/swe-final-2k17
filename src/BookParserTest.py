from BookParser import BookParser

''' Run this file to test BookParser '''
bp = BookParser()

''' Test file parser '''
# Will pass if the csv_to_dict_list method returns a list of dicts
def should_ret_list():
    result = 'should_ret_list: '
    book_list = bp.csv_to_dict_list()
    if len(book_list) > 0:
        print result +'PASS'
    else:
        print result +'FAIL'

''' Test search '''
#Will pass if the search_by_title fun returns one result
def should_ret_one_result():
    result = 'should_ret_one_result: '
    results = bp.search_by_title("Biotechnology")
    if len(results) == 1:
        print result +'PASS'
    else:
        print result +'FAIL'

#Will pass if the search_by_title fun returns nothing
def should_ret_nothing():
    result = 'should_ret_nothing: '
    search = bp.search_by_title("this string won't match!")
    if search == -1:
        print result +'PASS'
    else:
        print result +'FAIL'

#Will pass if the search_by_title fun returns one result
def should_ret_one_isbn():
    result = 'should_ret_one_isbn: '
    search = bp.search_by_isbn("978-0073511450")
    if len(search) == 1:
        search_res = search[0]
        if search_res[bp.TITLE] == "Essentials of Economics 3rd Edition":
            print result +'PASS'
        else:
            print result +'FAIL'

#Will pass if the search_by_prof fun returns one result
def should_ret_one_prof():
    result = 'should_ret_one_prof: '
    search = bp.search_by_prof("Lartigue")
    if len(search) == 1:
        print result +'PASS'
    else:
        print result +'FAIL'

#Will pass if the search_by_class fun returns one result for SWE
def should_ret_one_class():
    result = 'should_ret_one_class: '
    search = bp.search_by_class("SWE")
    if len(search) == 1:
        print result +'PASS'
    else:
        print result +'FAIL'

def should_ret_sixteen_kw():
    result = 'should_ret_16_description: '
    search = bp.search_by_desc("No description available")
    if len(search) == 16:
        print result +'PASS'
    else:
        print result +'FAIL'

def should_ret_available_types():
    result = 'should_ret_available_types: '
    book = bp.search_by_isbn('978-0300161632')[0]
    types = bp.types_for_book(book)
    if len(types) > 1:
        print result +'PASS'
    else:
        print result +'FAIL'

def should_ret_profs():
    result = 'should_ret_profs: '
    search = bp.get_list_of_prof()
    if len(search) > 0:
        print result +'PASS'
    else:
        print result +'FAIL'

def should_ret_auth_search():
    result = 'should_ret_auths: '
    search = bp.search_by_author('Baase')
    if len(search) > 0:
        return result +'PASS'
    else:
        return result +'FAIL'
#Should write new stock for book by isbn to books db
def should_write_new_stock():
    result = 'should_write_new_stock: '
    #Subtracts 10 from current stock
    bp.update_stock('978-0073376356', 'New', '10')
    book = bp.search_by_isbn('978-0073376356')[0]
    if book[bp.STOCK_RENT] == '5':
        print result +'PASS'
    else:
        print result +'FAIL'

''' Test dict index values '''
#Will pass if the value at the given index value matches the value name
def should_ret_value():
    result = 'should_ret_value: '
    book = bp.csv_to_dict_list()[1]
    book_title = book[bp.TITLE]
    if book_title == 'Essentials of Economics 3rd Edition':
        print result +'PASS'
    else:
        print result +'FAIL'

#This method is run when `python BookParserTest.py` is run
#It runs all test methods
def run_all_tests():
    should_ret_list()
    should_ret_one_result()
    should_ret_one_isbn()
    should_ret_one_prof()
    should_ret_one_class()
    should_ret_profs()
    should_write_new_stock()
    should_ret_available_types()
    should_ret_auth_search()
    should_ret_sixteen_kw()
    should_ret_nothing()
    should_ret_value()

run_all_tests()
