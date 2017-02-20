#!/usr/bin/env python
# -*- coding:utf-8 -*-

List = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45,5000]
big1,big2 = 0,0

for i in List:
    if i > big1:
        big1 = i

for i in List:
    if i == big1:
        continue
    if i > big2:
        big2 = i

print big1,big2
    

