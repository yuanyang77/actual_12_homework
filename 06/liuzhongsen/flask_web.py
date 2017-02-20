#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import Flask,request,render_template,redirect,session
import fileutil
fileutil.read_file()
app = Flask(__name__)
app.secret_key = 'lkjklj;sdf;lasiog;lkwoeilkkls;'

import MySQLdb as mysql
conn = mysql.connect(user='root',passwd='123456',host='127.0.0.1',db='reboot12')
conn.autocommit(True)
cur = conn.cursor()
#cur.execute('select * from woniu_user')
#print cur.fetchall()


@app.route('/')
def index():
    if 'username' in session:
        return redirect('/list')
    return render_template('login.html')

#@app.route('/login',methods=['GET','POST'])
#def login():
#    print request.method
#    if request.method == 'GET':
#        return render_template('login.html')
#    elif request.method 

@app.route('/logout')
def logout():
    session.pop('username')
    return redirect('/')

@app.route('/loginaction')
def login():
    user = request.args.get('user')
    pwd = request.args.get('pwd')
    error_msg = ''
    if user and pwd:
        if user == 'admin' and pwd == 'admin':
            session['username'] = 'admin'
            return redirect('/list')
        else:
            error_msg = 'wrong user or password'
    else:
        error_msg = 'need user and pwd'
    return render_template('login.html',error_msg = error_msg)

@app.route('/del')
def del_user():
    user = request.args.get('user')
    fileutil.file_dict.pop(user)
    fileutil.write_file()
    return redirect('/list')

@app.route('/update')
def update():
    user = request.args.get('user')
    pwd = fileutil.file_dict.get(user)
    return render_template('update.html',pwd=pwd,user=user)

@app.route('/updateaction')
def updateaction():
    new_pwd = request.args.get('new_pwd')
    user = request.args.get('user')
    fileutil.file_dict[user] = new_pwd
    fileutil.write_file()
    return redirect('/list')

@app.route('/adduser')
def adduser():
    user = request.args.get('user')
    pwd = request.args.get('pwd')

    if user in fileutil.file_dict:
        return redirect('/list')
    else:
        sql = 'insert into woniu_user values ("%s","%s")' % (user,pwd)
        cur.execute(sql)
        #fileutil.file_dict[user] = pwd
        #fileutil.write_file()
        return redirect('/list')

@app.route('/list')
def userlist():
    if 'username' in session:
        return render_template('list.html',userlist=fileutil.file_dict.items())
    else:
        return redirect('/')

if __name__ == '__main__':
    app.run(host = '0.0.0.0',port=9002,debug=True)

