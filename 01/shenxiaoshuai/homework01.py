#!/usr/bin/env python
# -*- coding: utf-8 -*-

list=[1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]
first=0
second=0
for i in list:
	if i > first:
		first=i
for i in list:
	if i > second and i <first:
		second=i
print 'top1= %s,top2= %s' %(first,second)