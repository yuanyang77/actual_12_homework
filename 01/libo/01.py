#coding=utf-8
a = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]
max_num = 0
min_num = 0
for i in a:
	if i > max_num:
	   
	   min_num = max_num
	   max_num = i
	elif i > min_num:
	   min_num = i
print "最大的两个值为:%s,%s" %(min_num,max_num)
