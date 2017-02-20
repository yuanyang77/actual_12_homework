#!/usr/bin/env python
# -*- coding:utf-8 -*-

from  flask import Flask,render_template,request,redirect,session
import db

app = Flask(__name__,static_folder='src')
app.secret_key = 'ABCDEFGHIGK'

@app.route('/')
def root():
	if 'admin' in session:
		return render_template('index.html', dict=db.alldbtodict())
	return render_template('login.html')

@app.route('/index.html',methods=['GET','POST'])
def index_html():
	if request.method == 'POST':
		username = request.form.get('username')
		password = request.form.get('password')
		if db.verifyadmin(username,password):
			session['admin'] = 'admin'
			return render_template('index.html',dict=db.alldbtodict())
		else:
			return render_template('login.html',msg='Your not admin !')
	else:
		if  'admin' in session:
			return render_template('index.html',dict=db.alldbtodict())
		else:
			return redirect('/')

@app.route('/logout')
def logout():
                session.pop('admin')
                return redirect('/')

@app.route('/modpasswd',methods=['GET','POST'])
def modpasswd():
	if request.method == 'POST':
		passwd = request.form.get('password')
		if passwd :
				username = request.form.get('username')
				db.modpass(username,passwd)
				return redirect('/index.html')
	else:
			username = request.args.get('user')
			return  render_template('modpassword.html',user=username)

@app.route('/deluser',methods=['GET','POST'])
def deluser():
		user = request.form.get('username')
		if user :
			db.deluser(user)
			return  render_template('index.html',dict=db.alldbtodict())

@app.route('/adduser',methods=['GET','POST'])
def adduser():
		if request.method == 'POST':
			username = request.form.get('username')
			passwd = request.form.get('password')
			db.adduser(username,passwd)
			return render_template('index.html', dict=db.alldbtodict())
		else:
			return render_template('adduser.html')

if __name__ == '__main__':
                app.run(host='0.0.0.0' ,port=1234 ,debug=True)
