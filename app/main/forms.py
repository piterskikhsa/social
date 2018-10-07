from flask.ext.wtf import FlaskForm

from wtforms import StringField, SubmitField, TextAreaField, BooleanField, SelectField
from wtforms.validators import Required, Length, Regexp, Email, ValidationError

from app.models import Role, User


class NameForm(FlaskForm):
    name = StringField("Ваше Имя?", validators=[Required()])
    submit = SubmitField("Submit")


class EditProfileForm(FlaskForm):
    name = StringField('Настроящие имя', validators=[Length(0, 64)])
    location = StringField('Адрес', validators=[Length(0, 64)])
    about_me = TextAreaField('Обо мне')
    submit = SubmitField('Submit')


class EditProfileAdminForm(FlaskForm):
    email = StringField('Email', validators=[Required(), Length(1,64), Email()])
    username = StringField('Логин', validators=[Required(), Length(3,64), Regexp('^[A-z][A-z0-9_\.]*$',0,
                                                                                 "Логин должен состоять из букв, цифр, _ .")])
    confirmed = BooleanField('Подтверждён')
    role = SelectField('Role', coerce=int)
    name = StringField('Настроящие имя', validators=[Length(0, 64)])
    location = StringField('Адрес', validators=[Length(0, 64)])
    about_me = TextAreaField('Обо мне')
    submit = SubmitField('Submit')

    def __init__(self, user, *args, **kwargs):
        super(EditProfileAdminForm, self).__init__(*args, **kwargs)
        self.role.choices = [(role.id, role.name) for role in Role.query.order_by(Role.name).all()]
        self.user = user

    def validate_email(self, field):
        if field.data != self.user.email and User.query.filter_by(email=field.data).first():
            raise ValidationError('Email уже существует')

    def validate_username(self, field):
        if field.data != self.user.username and User.query.filter_by(username=field.data).first():
            raise ValidationError('Логин уже существует')