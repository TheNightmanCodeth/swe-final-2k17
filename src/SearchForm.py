from wtforms import Form, StringField, SelectField, validators
from BookParser import BookParser

class SearchForm(Form):
    isbn = StringField('ISBN', validators=[validators.Optional()], filters=[lambda x: x or None])
    bp = BookParser()
    profs = [(book, book) for book in bp.get_list_of_prof()]
    prof = SelectField(u'Author', choices=profs, validators=[validators.Optional()], filters=[lambda x: x or None])
    title = StringField('Title', validators=[validators.Optional()], filters=[lambda x: x or None])
    classs = SelectField(u'Class', choices=[(book, book) for book in bp.get_list_of_classes()], validators=[validators.Optional()], filters=[lambda x: x or None])
    author = StringField(u'Author', validators=[validators.Optional()], filters=[lambda x: x or None])
    keyword = StringField('Keyword', validators=[validators.Optional()], filters=[lambda x: x or None])
