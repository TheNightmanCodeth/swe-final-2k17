from wtforms import Form, StringField, SelectField, validators, SelectMultipleField, PasswordField, BooleanField
from BookParser import BookParser

class BookTypeForm(Form):
    #TODO: get isbn from parent somehow
    bp = BookParser()
    types = [(types, types) for types in ['New', 'Used', 'Rent', 'E-book']]
    isbn = StringField(u'ISBN', validators=[validators.Required()], filters=[lambda x: x or None])
    types = SelectField(u'Types', choices=types, validators=[validators.Optional()], filters=[lambda x: x or None])
    search = SelectMultipleField(choices=[])

class SearchForm(Form):
    isbn = StringField('ISBN', validators=[validators.Optional()], filters=[lambda x: x or None])
    bp = BookParser()
    profs = [(book, book) for book in bp.get_list_of_prof()]
    prof = SelectField(u'Author', choices=profs, validators=[validators.Optional()], filters=[lambda x: x or None])
    title = StringField('Title', validators=[validators.Optional()], filters=[lambda x: x or None])
    classs = SelectField(u'Class', choices=[(book, book) for book in bp.get_list_of_classes()], validators=[validators.Optional()], filters=[lambda x: x or None])
    author = StringField(u'Author', validators=[validators.Optional()], filters=[lambda x: x or None])
    keyword = StringField('Keyword', validators=[validators.Optional()], filters=[lambda x: x or None])

class ShoppingCartForm(Form):
    qty = StringField(u'qty', validators=[validators.Required()], filters=[lambda x: x or None])
    isbn = StringField(u'ISBN', validators=[validators.Required()], filters=[lambda x: x or None])

class CheckoutForm(Form):
    #Billing
    same_as_shipping = BooleanField('Same as shipping:')
    billing_name = StringField(u'Name', validators=[validators.Optional()], filters=[lambda x: x or None])
    billing_addr = StringField(u'Address', validators=[validators.Optional()], filters=[lambda x: x or None])
    billing_city = StringField(u'City', validators=[validators.Optional()], filters=[lambda x: x or None])
    billing_state = StringField(u'State', validators=[validators.Optional()], filters=[lambda x: x or None])
    billing_zip = StringField(u'ZIP', validators=[validators.Optional()], filters=[lambda x: x or None])
    ''' Payment '''
    #Hidden field for storing payment type information
    payment_type = StringField(u'Payment', validators=[validators.Optional()], filters=[lambda x: x or None]) #Yes i know we don't /technically/ need the filters in a required field, but it's a fallback I guess.
    #PayPal
    pp_email = StringField(u'Email', validators=[validators.Optional(), validators.Email()], filters=[lambda x: x or None])
    pp_password = PasswordField(u'Password', validators=[validators.Optional()], filters=[lambda x: x or None])
    #Credit Card
    card = StringField(u'Card Number (No dashes!)', validators=[validators.Optional(), validators.Length(min=16)], filters=[lambda x: x or None])
    exp_m = StringField(u'MM', validators=[validators.Optional(), validators.Length(min=2, max=2)], filters=[lambda x: x or None])
    exp_y = StringField(u'YY', validators=[validators.Optional(), validators.Length(min=2, max=2)], filters=[lambda x: x or None])
    cvv   = StringField(u'CVV', validators=[validators.Optional(), validators.Length(min=3, max=3)], filters=[lambda x: x or None])
    #Financial Aid
    fa_login = StringField(u'Username', validators=[validators.Optional()], filters=[lambda x: x or None])
    fa_password = PasswordField(u'Password', validators=[validators.Optional()], filters=[lambda x: x or None])
    ''' Shipping '''
    #Shipping address
    shipping_name = StringField(u'Name', validators=[validators.Required()], filters=[lambda x: x or None], id="shipping_name")
    shipping_addr = StringField(u'Address', validators=[validators.Required()], filters=[lambda x: x or None], id="shipping_addr")
    shipping_city = StringField(u'City', validators=[validators.Required()], filters=[lambda x: x or None], id="shipping_city")
    shipping_state = StringField(u'State', validators=[validators.Required()], filters=[lambda x: x or None], id="shipping_state")
    shipping_zip = StringField(u'ZIP', validators=[validators.Required(), validators.Length(min=5, max=5)], filters=[lambda x: x or None], id="shipping_zip")
    #Email address for receipt
    email = StringField(u'Email', validators=[validators.Optional(), validators.Email()], filters=[lambda x: x or None], id="email")
