#!/usr/bin/env python
# -*- coding:utf-8 -*-

import MySQLdb as mysql

conn = mysql.connect(user='root',passwd='123456',host='127.0.0.1',db='zhoulouzi')
conn.autocommit(True)
cur = conn.cursor()

def verifyadmin(username,passwd):
		cur.execute('select password from accessdb where username = "admin"')
		temp = cur.fetchall()
		if passwd == temp[0][0]:
				return  True
		else:
				return False

def alldbtodict():
		cur.execute('select * from accessdb')
		temp=cur.fetchall()
		dict = {}
		for (user,passwd) in temp:
				dict[user] = passwd
		return dict

def modpass(username,passwd):
		temp = "update accessdb set password = '%s'  where username = '%s' " % (passwd,username)
		cur.execute(temp)

def deluser(username):
		temp = "DELETE FROM accessdb WHERE username = '%s' " % (username)
		cur.execute(temp)

def adduser(username,passwd):
		temp = "INSERT INTO accessdb VALUES  ('%s','%s')"  % (username,passwd)
		cur.execute(temp)
