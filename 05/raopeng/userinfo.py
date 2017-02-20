#!/usr/bin/env python
# -*- coding: utf-8 -*-
#    author:RaoPeng

def get_user():
	with open('user') as f:
		user_dict = {}
		for i in f.read().split('\n'):
			if i=='':
				continue
			else:
				user_dict[i.split(':')[0]] = i.split(':')[1]
		return user_dict

if __name__=='__main__':
	print get_user()
