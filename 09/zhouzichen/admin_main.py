#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Flask,render_template,redirect,url_for,request,session


app = Flask(__name__,static_folder='static')
app.secret_key = 'zhoulouziABCDEFG'

@app.route('/')
def root():
	return redirect(url_for('index'))

@app.route('/login',methods=['POST','GET'])
def login():
	if request.method == 'POST':
		session['username']  = request.form['username']
		return redirect(url_for('index'))
	else:
		return render_template('login.html')

@app.route('/logout')
def logout():
	session.pop('username',None)
	return redirect(url_for('login'))

@app.route('/index')
def index():
	if 'username' in session:
			return render_template('index.html')
	return redirect(url_for('login'))

if __name__ =='__main__':
	app.run(host='0.0.0.0',port=80,debug=True)