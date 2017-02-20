#/usr/bin/env python
#coding:utf-8

L = [9,8,7,6,5,4,3,2,1]

for x in range(1,len(L)):
    for i in range(x-1,-1,-1):
        if L[i] > L[i+1]:
            temp = L[i+1]
            L[i+1] = L[i]
            L[i] = temp 
        print L

#直接插入排序
