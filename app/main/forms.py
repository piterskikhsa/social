from flask.ext.wtf import FlaskForm

from wtforms import StringField, SubmitField
from wtforms.validators import Required


class NameForm(FlaskForm):
    name = StringField("Ваше Имя?", validators=[Required()])
    submit = SubmitField("Submit")