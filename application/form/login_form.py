#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:shenhaodong
# datetime:2020-07-26 13:57
# software: PyCharm


from flask_wtf import FlaskForm as Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired


class LoginForm(Form):
    accountNumber = StringField('accountNumber', validators=[DataRequired('accountNumber is null')])
    password = PasswordField('password', validators=[DataRequired('password is null')])