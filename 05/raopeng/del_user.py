#!/usr/bin/env python
# -*- coding:utf-8 -*-
#   author:RaoPeng

def mo_dict(user):
	user_dict = {}
	with open('user','a+') as f:
		for i in f.read().split('\n'):
			if i=='':
				continue
			else:
				user_dict[i.split(':')[0]] = i.split(':')[1]
		user_dict.pop(user)
	return user_dict

def del_u(user):
	user_dict = mo_dict(user=user)
	with open('user','w') as f:
		for i in user_dict:
			user_str = i+':'+user_dict[i]+'\n'
			f.write(user_str)

if __name__=='__main__':
	print del_u(user='123')


