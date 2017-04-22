from wtforms import Form, StringField, SelectField, validators, SelectMultipleField
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
