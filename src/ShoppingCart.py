from flask import g
from app import app

class ShoppingCart:

    def get_cart(self):
        with app.app_context():
            return g.cart

    def add_to_cart(self, book):
        with app.app_context():
            g.cart = g.cart.append(book)
