#!/usr/bin/python  
# -*- coding: utf-8 -*-  
####课上的
user = raw_input('user:')
pwd = raw_input('pwd:')
f = open('/home/wangyw/1.txt')
arr = f.read().split('\n')
#print arr
f.close

user_exists = False
for u in arr:
    temp = u.split(':')
#    print temp
    if temp[1] == user or temp[0] == user:
        if temp[2] == pwd:
            msg = 'login success'
        else:
            msg = 'pwd wrong'
        user_exists = True
        print msg
        break
if not user_exists:
    print 'user not exits'

##冒泡排序 http://blog.csdn.net/onlyanyz/article/details/45177643  参考的算法讲解
unsortedList = [1 , 2 , 3 , 2 , 12 , 3 , 1 , 3 , 21 , 2 , 2 , 3 , 4111 , 22 , 3333 , 444 , 111 , 4 , 5 , 777 , 65555 ,
                45 , 33 , 45]
count = 0 
def bubbleSort(unsortedList):
	list_length = len(unsortedList)
	for i in range(0,list_length-1):
	    for j in range(0,list_length-i-1):
		if unsortedList[j]>unsortedList[j+1]:
		    unsortedList[j],unsortedList[j+1]=unsortedList[j+1],unsortedList[j]
	return unsortedList
print(bubbleSort(unsortedList))
