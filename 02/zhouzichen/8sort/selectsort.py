#/usr/bin/env python
#coding:utf-8

L = [9,8,7,6,5,4,3,2,1]

for x in range(0,len(L)):
    mininum = L[x]
    for i in range(x+1,len(L)):
        if L[i] < mininum:
            temp = L[i]
            L[i] = mininum
            mininum = temp
    L[x] = mininum
    print L
