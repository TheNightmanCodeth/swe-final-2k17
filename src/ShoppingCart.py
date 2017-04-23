from flask import session

class ShoppingCart:

    def get_cart(self):
        return session['cart']

    def get_cart_subtotal(self):
        subtotal = 0
        for entry in session['cart']:
            price = entry['price']
            qty = entry['count']
            subtotal += float(price) * int(qty)
        return subtotal
        
    def delete_item(self, form_isbn):
        index = 0
        cart = session['cart']
        for entry in cart:
            isbn = entry['book'][0]
            if form_isbn == isbn:
                del cart[index]
            index += 1
        return cart

    def edit_item_qty(self, isbn, qty):
        new_qty = int(qty)
        cart = session['cart']
        for entry in cart:
            entry_isbn = entry['book'][0]
            if isbn == entry_isbn:
                if qty == '0':
                    cart = self.delete_item(isbn)
                else:
                    entry['count'] = qty
        return cart

    def get_cart_size(self):
        return len(session['cart'])
