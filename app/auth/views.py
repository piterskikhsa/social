from flask import render_template, redirect, request, url_for, flash
from flask.ext.login import login_user, login_required, logout_user

from . import auth
from .forms import LoginForm, RegistrationForm
from ..models import User
from ..email import send_email
from .. import db


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('Неверный Логин или Пароль')

    return render_template('auth/login.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Вы вышли, до скорой встречи')
    return redirect(url_for('main.index'))


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data, username=form.username.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        token = user.generate_confirmation_token()
        send_email(user.email, 'Подтвердите ваш email', 'auth/email/confirm', user=user, token=token)
        flash('Письмо с подтверждением отправлено вам по электронной почте')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)


