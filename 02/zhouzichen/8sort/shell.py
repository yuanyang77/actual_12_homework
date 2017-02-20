#!/usr/bin/env python
#coding:utf-8

L = [9,8,7,6,5,4,3,2,1]

gap = int(len(L)/2)

while gap >= 1 :
    for x in range(gap,len(L)):
        for i in range(x-gap,-1,-gap):
            if L[i] > L[i+gap]:
                temp = L[i+gap]
                L[i+gap] = L[i]
                L[i] = temp
            print L
    gap = int(gap/2)

