#!/usr/bin/env python
# -*- coding:utf-8 -*-

import  userdbtodict

def verifyuser(username,passwd):
		admin_user = { 'admin' :  'admin'}
		user_dict = userdbtodict.userdb()
		if  username in admin_user :
				if admin_user[username] == passwd:
					return 1   # 1 代表admin账号密码都正确。2代表密码错误  3 代表普通用户验证成功 0表示用户不存在
				else:
					return 2
		####这块没有做的那么详细。待开发。
		elif  username in user_dict:
				if user_dict[username] == passwd:
					return 3
				else:
					return 2
		else:
				return 0
