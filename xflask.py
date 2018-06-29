#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 引入 Flask 类，Flask 类实现了一个 WSGI 应用。
from flask import Flask
from flask import make_response
from flask import redirect
from flask import render_template
from flask_script import Manager
from flask_bootstrap import Bootstrap


# app 是 Flask 类的实例，接收包或者模块的名字作为参数，但一般都是传递 __name__。
app = Flask(__name__)
manager = Manager(app)
bootstrap = Bootstrap(app)


# 使用程序实例提供的 app.route 修饰器，将修饰的 index() 函数注册为程序根地址的处理程序。
@app.route('/')
def index():
    '''
    #
    user_agent = request.headers.get('User-Agent')
    return '<h1>Hello World!</h1>' + '<p>Your Browser is %s</p>' % user_agent
    '''
    return render_template('index.html')


@app.route('/user/<name>')
def user(name):
    # Flask 默认设置的响应状态码为：200，表示请求已经被成功处理。
    # return '<h1>Hello, %s</h1>' % name, 400
    return render_template('user.html', name=name)


# 使用 response 对象作为响应体
@app.route('/response')
def xdhuxc_response():
    response = make_response('<h1>This document carries a cookie</h1>')
    response.set_cookie('answer', '422')
    return response


# 重定向，状态码 302
@app.route('/redirect')
def xdhuxc_redirect():
    return redirect('www.baidu.com')


# __name__ == '__main__' 是 Python 的惯常用法，在这里确保直接执行这个脚本时才会启动开发 web 服务器。
if __name__ == '__main__':
    manager.run()
