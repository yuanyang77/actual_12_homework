#!/usr/bin/env python
# -*- coding:utf-8 -*-

import MySQLdb as mysql
import passwd_hash

conn = mysql.connect(user='root',passwd='123456',host='127.0.0.1',db='zhoulouzi')
conn.autocommit(True)
cur = conn.cursor()
user_info_db = 'accessdb'


def register_user(username,passwd):
	hashed = passwd_hash.encrypt_password(passwd)
	temp = "INSERT INTO %s(username,password) VALUES  ('%s','%s')" % (user_info_db,username, hashed)
	cur.execute(temp)

def verify_user(username,passwd):
	cur.execute('select password from %s where username = "%s"' % (user_info_db,username))
	hashed = cur.fetchall()
	if passwd_hash.validate_password(hashed[0][0],passwd):
			return True
	else:
			return False

def update_user(username,password):
	hashed = passwd_hash.encrypt_password(password)
	cur.execute('update %s set password = "%s" where username = "%s"' % (user_info_db,hashed,username))
	return True

if __name__ == '__main__':
		#register_user('admin','admin')
		print verify_user('admin','admin')

