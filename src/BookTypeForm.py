from wtforms import Form, StringField, SelectField, validators, SelectMultipleField
from BookParser import BookParser

class BookTypeForm(Form):
    #TODO: get isbn from parent somehow
    bp = BookParser()
    types = [(types, types) for types in ['New', 'Used', 'Rent', 'E-book']]
    isbn = StringField(u'ISBN', validators=[validators.Required()], filters=[lambda x: x or None])
    types = SelectField(u'Types', choices=types, validators=[validators.Optional()], filters=[lambda x: x or None])
    search = SelectMultipleField(choices=[])
