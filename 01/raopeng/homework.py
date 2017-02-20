#!/usr/bin/env python
#coding:utf8

#第一种简单粗暴方法
arr = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]
f_max_num = 0
f_sec_num = 0
for num1 in arr:
	if num1 > f_max_num:
		f_max_num = num1
for num2 in arr:
	if num2 > f_sec_num and num2 < f_max_num:
		f_sec_num = num2
print 'max num is %s,sec num is %s' %(f_max_num,f_sec_num)
print '='*50

#第二种方法,当最大值有相等的两个数时
brr = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,65555,45,33,45]
a = 0
b = 0
for i in brr:
	if i > a:
		b = a
		a = i
		#print a,b
	elif i >= b:
		b = i
		#print b
#print '*'*30
print 'max num is %s,sec num is %s' %(a,b)
