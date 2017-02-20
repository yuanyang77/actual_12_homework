#coding=utf-8
arr = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]
max1_num = 0
max2_num = 0
for i in arr:
	if i > max1_num:
		max2_num = max1_num
		max1_num = i
	elif i > max2_num:
		max2_num = i
print max1_num , max2_num
