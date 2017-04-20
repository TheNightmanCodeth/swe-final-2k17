from wtforms import Form, StringField, SelectField, validators
from BookParser import BookParser

class BookTypeForm(Form):
    #TODO: get isbn from parent somehow
    types = SelectField(u'Types', choices=profs, validators=[validators.Optional()], filters=[lambda x: x or None])
