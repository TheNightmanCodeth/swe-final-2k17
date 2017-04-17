from wtforms import Form, StringField, validators

class SearchForm(Form):
    isbn = StringField('ISBN', validators=[validators.Optional()], filters=[lambda x: x or None])
    prof = StringField('Professor', validators=[validators.Optional()], filters=[lambda x: x or None])
