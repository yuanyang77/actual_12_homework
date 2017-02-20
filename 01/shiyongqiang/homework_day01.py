#!/usr/bin/python


_list=[1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]
max1=0
max2=0
for i in _list:
	for j in _list:
		if max1 < i:
			max1=i
		if max1 > j and j > max2:
			max2=j
print 'The first big number: %s. Second big numbers: %s' %(max1,max2)	