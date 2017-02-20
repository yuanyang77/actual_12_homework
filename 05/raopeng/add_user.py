#!/usr/bin/env python
# -*- coding:utf-8 -*-
#   author:RaoPeng

def add_u(user,pwd):
	with open ('user','a') as f:
		user_str = user+':'+pwd+'\n'
		f.write(user_str)

if __name__=='__main__':
	add_u(user='rp',pwd='123')
