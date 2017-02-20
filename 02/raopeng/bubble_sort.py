#coding:utf8
arr = [3,7,18,2,20,99,1,54,123,4,1000,2300]
print arr
count = 0
length = len(arr)-1
for j in range(length):
	for i in range(length-j):
		if arr[i]>arr[i+1]:
			arr[i],arr[i+1] = arr[i+1],arr[i]
		count +=1
	print '+'*30
	print arr
print '循环了%s次' %(count)
