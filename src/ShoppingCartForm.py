from wtforms import Form, StringField, validators
from BookParser import BookParser

class ShoppingCartForm(Form):
    qty = StringField(u'qty', validators=[validators.Required()], filters=[lambda x: x or None])
    isbn = StringField(u'ISBN', validators=[validators.Required()], filters=[lambda x: x or None])
