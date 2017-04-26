from ShoppingCart import ShoppingCart
from BookParser import BookParser

sc = ShoppingCart()
bp = BookParser()

''' Tests shopping cart methods '''

def should_add_book():
    res = 'should_add_book: '
    cart = len(sc.get_cart())
    book = bp.search_by_isbn('978-0205734610')[0]
    sc.add_to_cart(book)
    if len(sc.get_cart()) > cart:
        print res +'PASS'
    else:
        print sc.get_cart()
        print res +'FAIL'

def run_all_tests():
    should_add_book()

run_all_tests()
