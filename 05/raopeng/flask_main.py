#!/usr/bin/env python
# -*- coding: utf-8 -*-
#    author:RaoPeng

from flask import Flask,request,render_template,redirect
import userinfo
import check_user
from add_user import add_u
from del_user import del_u
app = Flask(__name__)

#渲染登录界面
@app.route('/')
def login():
	return render_template('index.html')

#登录判断并跳转
@app.route('/login')
def admin_show():
	user = request.args.get("user")
	pwd = request.args.get("password")
	#res = check_user.check(user=user,pwd=pwd)
	if check_user.check(user=user,pwd=pwd)==0:
		return redirect('/userinfo')
	else:
		return redirect('/error')

#显示用户信息界面
@app.route('/userinfo')
def show_user_info():
	user_dict = userinfo.get_user()
	return render_template('userinfo.html',udict=user_dict)

#显示添加用户名和密码界面
@app.route('/show_add')
def show_add():
	return render_template('adduser.html')

#添加成功跳转到用户信息界面
@app.route('/adduser')
def add_user():
	user = request.args.get("user")
	pwd = request.args.get("password")
	add_u(user=user,pwd=pwd)
	return redirect('/userinfo')

#显示删除用户界面
@app.route('/show_del')
def show_del():
	return render_template('deluser.html')

#删除成功跳转到用户信息界面
@app.route('/deluser')
def del_user():
	user = request.args.get("user")
	del_u(user=user)
	return redirect('/userinfo')

#登录错误的错误界面
@app.route('/error')
def error_info():
	return '<img width="50%" src="http://imgsrc.baidu.com/forum/w=580/sign=dfb78efe0c7b02080cc93fe952d8f25f/7f118701a18b87d696ce0d44010828381e30fdef.jpg">'


if __name__=='__main__':
	app.run(host='0.0.0.0',port=10008,debug=True)
