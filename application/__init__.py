#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:shenhaodong
# datetime:2020-07-26 13:35
# software: PyCharm

from flask import Flask
from application.config import config
from application.model import *

def creat_app(config_name):
    app = Flask(__name__)
    login_manager.init_app(app)
    if config_name is not None:
        app.config.from_object(config[config_name])
        db.init_app(app)

    #
    with app.app_context():
        db.create_all()
    @app.route('/')
    def hello():
        return "hello wrold"


    return app



