'''Yes I know that's not what a factory is'''
import datetime
from random import randint
from flask import session
from ShoppingCart import ShoppingCart
from BookParser import BookParser

class InvoiceFactory:
    bp = BookParser()

    #Takes a dict with invoice data and writes it to a file
    def write_to_file(self, invoice):
        timestamp = '{:%Y-%m-%d}'.format(datetime.datetime.now())
        time = '{:%H%M%S}'.format(datetime.datetime.now())

        filename = timestamp +' ' +time
        file_to_write = open('shared/{}.txt'.format(filename), 'w+')
        file_to_write.write('Date placed: ' +timestamp +'\n')
        if invoice['type'] == 'pp':
            file_to_write.write('Payment type: PayPal\n')
        elif invoice['type'] == 'cc':
            file_to_write.write('Payment type: Credit Card\n')
        elif invoice['type'] == 'fa':
            file_to_write.write('Payment type: Financial Aid\n')
        file_to_write.write('---Shipping---\n')
        file_to_write.write('Name: ' +invoice['ship_name'] +'\n')
        file_to_write.write('Address: ' +invoice['ship_addr'] +'\n')
        file_to_write.write('State: ' +invoice['ship_state'] +'\n')
        file_to_write.write('City: ' +invoice['ship_city'] +'\n')
        file_to_write.write('Zip: ' +invoice['ship_zip'] +'\n')
        file_to_write.write('---Books---\n')
        for entry in session['cart']:
            book = entry['book']
            file_to_write.write(book[0] +': ' +book[1] +' (' +entry['type'] +')' +' $' +entry['price'] +' X ' +str(entry['count']) +'\n')
        file_to_write.write('---Financial---\n')
        sub_round = '%0.2f' % invoice['subtotal']
        tax_round = '%0.2f' % invoice['tax']
        total_round = '%0.2f' % invoice['total']
        file_to_write.write('Subtotal: ' +str(sub_round) +'\n')
        file_to_write.write('Sales tax: ' +str(tax_round) +'\n')
        file_to_write.write('Total: ' +str(total_round) +'\n')
    #Takes checkout info and returns a dict object
    def checkout_to_invoice(self, checkout_form):
        '''Payment'''
        dictionary = {}
        dictionary['type'] = checkout_form.payment_type.data
        if dictionary['type'] == 'pp':
            #PayPal!
            dictionary['pp_email'] = checkout_form.pp_email.data
            dictionary['pp_password'] = checkout_form.pp_password.data

        elif dictionary['type'] == 'cc':
            #Credit Card!
            dictionary['cc_number'] = checkout_form.card.data
            dictionary['cc_exp_m']  = checkout_form.exp_m.data
            dictionary['cc_exp_y']  = checkout_form.exp_y.data
            dictionary['cc_cvv']    = checkout_form.cvv.data
        elif dictionary['type'] == 'fa':
            #Financial aid!
            dictionary['fa_login'] = checkout_form.fa_login.data
            dictionary['fa_password'] = checkout_form.fa_password.data
        '''Shipping'''
        dictionary['ship_name'] = checkout_form.shipping_name.data
        dictionary['ship_addr'] = checkout_form.shipping_addr.data
        dictionary['ship_state'] = checkout_form.shipping_state.data
        dictionary['ship_city']  = checkout_form.shipping_city.data
        dictionary['ship_zip'] = checkout_form.shipping_zip.data

        '''Billing Address'''
        billing = checkout_form.same_as_shipping.data
        dictionary['same_as_shipping'] = str(billing)
        if billing:
            dictionary['bill_name'] = dictionary['ship_name']
            dictionary['bill_addr'] = dictionary['ship_addr']
            dictionary['bill_state'] = dictionary['ship_state']
            dictionary['bill_city'] = dictionary['ship_city']
            dictionary['bill_zip'] = dictionary['ship_zip']
        else:
            dictionary['bill_name'] = checkout_form.billing_name.data
            dictionary['bill_addr'] = checkout_form.billing_addr.data
            dictionary['bill_state'] = checkout_form.billing_state.data
            dictionary['bill_city'] = checkout_form.billing_city.data
            dictionary['bill_zip'] = checkout_form.billing_zip.data
        ''' Financial '''
        sc = ShoppingCart()
        st = sc.get_cart_subtotal()
        s_t = float(st) + 14.99
        tax = float(s_t) * .07
        total = s_t + tax
        dictionary['subtotal'] = st
        dictionary['total'] = total
        dictionary['tax'] = tax

        return dictionary

    def get_users(self):
        students = []
        f = file("files/students.txt").read()
        index = 0
        users = []
        user = []
        for word in f.split():
            if index < 4:
                user.append(word)
                index += 1
            else:
                user.append(word)
                index = 0
                users.append(user)
                user = []
        return users

    def verify_qty(self, book):
        cart = session['cart']
        stock = True
        for entry in cart:
            cart_book = entry['book']
            cart_book_type = entry['type']
            book = bp.search_by_isbn(cart_book[0])[0]
            if cart_book_type == 'New':
                if int(book[bp.STOCK_NEW]) <= 0:
                    stock = False
            if cart_book_type == 'Used':
                if int(book[bp.STOCK]) <= 0:
                    stock = False
            if cart_book_type == 'Rent':
                if int(book[bp.STOCK]) <= 0:
                    stock = False
        return stock
