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

''' Test title search '''
#Will pass if the search_by_title fun returns one result (expected behavior)
def should_ret_one_result():
    result = 'should_ret_one_result: '
    results = bp.search_by_title("Biotechnology")
    if len(results) == 1:
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
    should_ret_value()

if __name__ == "__main__":
    run_all_tests()
