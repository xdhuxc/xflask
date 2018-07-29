#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 引入 Flask 类，Flask 类实现了一个 WSGI 应用。
from flask import Flask
from flask import make_response
from flask import redirect
from flask import render_template
from flask import url_for
from flask import session
from flask import flash
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime


from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required

"""
为了实现CSRF保护，Flask-WTF需要程序设置一个秘钥。Flask-WTF使用这个秘钥生成加密令牌，再用令牌验证请求中表单数据的真伪，
"""

# app 是 Flask 类的实例，接收包或者模块的名字作为参数，但一般都是传递 __name__。
app = Flask(__name__)
"""
app.config 字典可用来存储框架、扩展和程序本身的配置变量
SECRET_KEY配置变量是通用秘钥，可在Flask和多个第三方扩展中使用，加密的强度取决于变量值的机密程度。
"""
app.config['SECRET_KEY'] = 'xdhuxc-hardly'
manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)


class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')


# 使用程序实例提供的 app.route 修饰器，将修饰的 index() 函数注册为程序根地址的处理程序。
"""
app.route 修饰器中添加的 methods 参数告诉Flask在URL映射中把这个视图函数注册为 GET 和 POST 请求的处理程序。
如果没有指定 methods 参数，就只把视图函数注册为 GET 请求的处理程序
"""


@app.route('/1', methods=['GET', 'POST'])
def index_1():
    '''
    #
    user_agent = request.headers.get('User-Agent')
    return '<h1>Hello World!</h1>' + '<p>Your Browser is %s</p>' % user_agent
    '''

    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    # return render_template('index.html', current_time=datetime.utcnow())
    return render_template('index.html', form=form, name=name, current_time=datetime.utcnow())


@app.route('/2', methods=['GET', 'POST'])
def index_2():
    form = NameForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        """
        推荐使用 url_for() 生成 URL，因为这个函数使用 URL 映射生成 URL，从而保证 URL 和定义的路由兼容，而且修改路由名字后依然可用。
        url_for() 函数的第一个且唯一必须指定的参数是端点名，即路由的内部名字。
        默认情况下，路由的端点是相应视图函数的名字。
        在此处，处理根地址的视图函数是 index()，因此传给 url_for() 函数的名字是 index
        """
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'), current_time=datetime.utcnow())


@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        print(old_name)
        if old_name and old_name != form.name.data:
            flash('Looks like you have changed your name. current is %s' % form.name.data)
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'), current_time=datetime.utcnow())


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


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500





# __name__ == '__main__' 是 Python 的惯常用法，在这里确保直接执行这个脚本时才会启动开发 web 服务器。
if __name__ == '__main__':
    manager.run()
