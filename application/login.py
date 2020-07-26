#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:shenhaodong
# datetime:2020-07-26 16:20
# software: PyCharm


from flask import render_template, request, redirect, Flask, url_for,Blueprint
from flask_login import login_user, login_required
from application.model.user_model import User
from application.model import login_manager
from application.form.login_form import LoginForm

userRoute = Blueprint('user', __name__, url_prefix='/user', template_folder='templates', static_folder='static')


@login_manager.user_loader
def load_user(user_id):
    # return User.user_id
    print('load_user;{}'.format(User.query.get(int(user_id))))
    return User.query.get(int(user_id))


@userRoute.before_request
def before_request():
    pass


@userRoute.route('/success')
@login_required
def index():
    return render_template('success.html')


@userRoute.route('/login', methods=['GET', 'POST'])
def login():
    print(123123)
    form = LoginForm()
    print("form:{}".format(form))
    if request.method == 'POST':
        print(request.form)

        if not form.validate_on_submit():
            print('form.error:{}'.format(form.errors))

            return render_template('login.html', form=form)

        user = User.query.filter(User.accountNumber == form.accountNumber.data,
                                 User.password == form.password.data).first()
        print('user :{}'.format(user))
        if user:
            login_user(user)
            print("afsdfsdafsdafsdfsdf")
            return redirect(url_for('user.index'))


    return render_template('login.html', form=form)