#!/usr/bin/env python
#coding=utf-8
from flask import Flask,request,render_template,redirect
import add_del_file
app = Flask(__name__)

##首页登录
@app.route('/')
def index():
    return render_template('login.html')

##验证用户名,密码
def check_login(user,pwd):
    if user == 'admin' and pwd == 'pwd':
        return redirect('/userlist')
    else:
        return redirect('/error')
##登录判断
@app.route('/login')
def login():
    user = request.args.get('user')
    pwd = request.args.get('pass')
    return check_login(user,pwd)

##用户列表界面
@app.route('/userlist')
def ulist():
    user = add_del_file.select_user()
    return render_template('user.html',names=user)

##注册用户
@app.route('/useradd')
def add_user():
    user = request.args.get('name')
    pwd = request.args.get('password')
    if user not in add_del_file.select_user():
        add_del_file.insert_user(user,pwd)
    else:
        pass
    return redirect("/userlist")

##删除用户
@app.route('/deluser')
def del_user():
    user = request.args.get('name')
    add_del_file.delete_user(user)
    return redirect('userlist')

##登录错误界面
@app.route('/error')
def err():
    return 'error 404'

if __name__=='__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)
