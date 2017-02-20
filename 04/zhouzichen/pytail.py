#!/usr/env/bin python
# coding:utf-8

import  time

def tail(filename):
	with open(filename,'r') as file:
		file.seek(0,2)
		while True:
			temp = file.readline()
			if temp:
				print temp
			else:
				time.sleep(1)

def tenprint(filename):
	with open(filename,'r') as file:
		#seek_num = 100
		#line_num = 10
		#while True:
				#if  file.tell() < seek_num * line_num:
						#print file.readlines()
						#break
				#else:
		print file.readlines()[-10:]

if __name__ == '__main__':
	tenprint('deflogansis.py')
	tail('deflogansis.py')






