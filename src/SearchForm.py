from wtforms import Form, StringField, validators

class SearchForm(Form):
    isbn = StringField('ISBN', validators=[validators.Optional()], filters=[lambda x: x or None])
    prof = StringField('Professor', validators=[validators.Optional()], filters=[lambda x: x or None])
    title = StringField('Title', validators=[validators.Optional()], filters=[lambda x: x or None])
    classs = StringField('Class', validators=[validators.Optional()], filters=[lambda x: x or None])
    keyword = StringField('Keyword', validators=[validators.Optional()], filters=[lambda x: x or None])