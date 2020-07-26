#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:shenhaodong
# datetime:2020-07-26 16:25
# software: PyCharm


from application.login import userRoute
from application import  creat_app

DEFAULT_MODULES = [userRoute]

app = creat_app('production')

for module in DEFAULT_MODULES:
    app.register_blueprint(module)


@app.before_request
def before_request():
    pass


if __name__ == '__main__':
    app.run(debug=True)