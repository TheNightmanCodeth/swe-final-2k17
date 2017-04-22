from wtforms import Form, StringField, SelectField, validators, SelectMultipleField
from BookParser import BookParser

class ShoppingCartForm(Form):
    qty = StringField(u'ISBN', validators=[validators.Required()], filters=[lambda x: x or None])
