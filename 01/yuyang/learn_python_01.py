#!/usr/bin/python
#coding=utf-8
###第一个实现，感觉应该还有更好的办法这个很low####

Arr_new = [102222222220,2000,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,452222]
max_num = 0
max_num2 = 0
for x in Arr_new:
    if x > max_num:
        max_num = x
s = Arr_new.index(max_num)
Arr_new.pop(s)
for y in Arr_new:
    if y > max_num2:
        max_num2 = y
s1 = Arr_new.index(max_num2)
Arr_new.pop(s1)
print 'Max_numer one is:',max_num,'Max_numer secoud is:',max_num2

###第二个。。。。

Arr_new = [102222222220,2000,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,42121]
max_num = 0
max_num2 = 0

for x in Arr_new:
    if x > max_num:
        max_num = x
for b in Arr_new:
    if b == max_num:
        continue
    elif b < max_num:
        max_num2 = b
print 'Max_numer one is:',max_num,'Max_numer secoud is:',max_num2