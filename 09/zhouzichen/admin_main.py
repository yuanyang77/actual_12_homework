#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Flask,render_template

app = Flask(__name__,static_folder='static')
app.secret_key = 'zhoulouziABCDEFG'

@app.route('/')
def root():
	return render_template('login.html')



if __name__ =='__main__':
	app.run(host='0.0.0.0',port=1234,debug=True)