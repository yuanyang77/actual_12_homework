#!/usr/bin/env python
# -*- coding:utf-8 -*-

def userdb():
	user_dict = {}
	with open('userkey.txt', 'r') as file:
		for line in file.read().split('\n'):
			if line:
				temp = line.split(':')
				user_dict[temp[0]] = temp[1]
	return user_dict

def moddb(user_dict):
		with open('userkey.txt','w') as file:
				for user in user_dict:
						temp = user + ':' + user_dict[user] + '\n'
						file.write(temp)


