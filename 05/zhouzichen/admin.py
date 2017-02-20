#!/usr/bin/env python
# -*- coding:utf-8 -*-

from  flask import Flask,render_template,request,redirect,session
import verify,userdbtodict,moduserdb

app = Flask(__name__)
app.secret_key = 'ABCDEFGHIGK'

@app.route('/portal')
def admin_html():
	return render_template('portal.html',name ='admin',userpasswd=userdbtodict.userdb())

@app.route('/')
def index():
	if 'admin' in session:
			return redirect('/portal')
	return  render_template('login.html')

@app.route('/login')
def login():
		username = request.args.get('username')
		passwd = request.args.get('passwd')
		if verify.verifyuser(username,passwd) == 1:
				session['admin'] = 'admin'
				return redirect('/portal')
		else:
				return 'not admin'

@app.route('/logout')
def logout():
		session.pop('admin')
		return redirect('/')

@app.route('/modpasswd')
def modpasswd():
		if request.args.get('passwd') :
				username = request.args.get('username')
				passwd = request.args.get('passwd')
				moduserdb.modpass(username,passwd)
				return redirect('/portal')
		else:
			username = request.args.get('user')
			return  render_template('modpasswd.html',user=username)

@app.route('/moduser')
def moduser():
		if request.args.get('action') == 'del' :
				user = request.args.get('user')
				moduserdb.deluser(user)
				return redirect('/portal')
		elif request.args.get('action') == 'add':
				return render_template('adduser.html')
		else:
			user = request.args.get('username')
			passwd = request.args.get('passwd')
			moduserdb.modpass(user,passwd)
			return redirect('/portal')

if __name__ == '__main__':
		app.run(host='0.0.0.0' ,port=1234 ,debug=True)