#!/usr/bin/env python
#encoding=UTF-8
num = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]
first = 0
second = 0
for i in num:
    if first < i :
        first = i
for i in num:
    if i != first and second < i:
        second = i
print first,second 
