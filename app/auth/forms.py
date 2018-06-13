from flask.ext.wtf import FlaskForm as Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Email, Length, Regexp, EqualTo
from wtforms import ValidationError

from ..models import User


class LoginForm(Form):
    email = StringField('Email', validators=[Required(), Length(1,64), Email()])
    password = PasswordField('Password', validators=[Required()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log in')


class RegistrationForm(Form):
    email = StringField('Email', validators=[Required(), Length(1,64), Email()])
    username = StringField('Username', validators=[Required(), Length(1,64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                                                                    'Имя пользователя иожет содержать '
                                                                                    'буквы, цыфры или _')])
    password = PasswordField('Password', validators=[Required(), EqualTo('password2', message='Пароли должны совпадать')])
    password2 = PasswordField('Confirm password', validators=[Required()])
    submit = SubmitField('Регистрация')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError("Пользователь с таким Email уже существует")

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Пользователь с таким Именем уже существует')