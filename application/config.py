#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:shenhaodong
# datetime:2020-07-26 13:38
# software: PyCharm
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'fjdlj324fs5ssjflKzcznv*c'
    DEBUG = False
    DB_USER = 'root'
    DB_PASSWORD = '123'
    DB_HOST = '122.51.192.201'
    DB_DB = 'test'
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://' + DB_USER + ':' + DB_PASSWORD + '@' + DB_HOST + '/' + DB_DB +'?charset=utf8'





    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:1011@localhost/rl_project?charset=utf8'


class DevelopmentConfig(Config):
    DEBUG = True
    DB_USER = 'root'
    DB_PASSWORD = '123'
    DB_HOST = '122.51.192.201'
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    DB_DB = 'zwc'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://' + DB_USER + ':' + DB_PASSWORD + '@' + DB_HOST + '/' + DB_DB +'?charset=utf8'




class ProductionConfig(Config):
    pass


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}


