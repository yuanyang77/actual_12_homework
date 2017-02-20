#!/usr/bin/env python
# -*- coding:utf-8 -*-

import userdbtodict

def modpass(username,passwd):
		user_dict = userdbtodict.userdb()
		user_dict[username] = passwd
		return userdbtodict.moddb(user_dict)

def deluser(user):
		user_dict = userdbtodict.userdb()
		del user_dict[user]
		return userdbtodict.moddb(user_dict)
