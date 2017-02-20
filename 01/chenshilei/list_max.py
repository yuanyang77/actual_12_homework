#!/usr/bin/evn python
#_*_ coding:utf-8 _*_

#search the first max  and the second max
_list=[1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]

#print _list
max_a=_list[0]
max_b=0
temp=0
for n in _list:
    if n > max_a:
        temp=max_a
        max_a=n
        max_b=temp
    elif n != max_a and n> max_b:
        max_b=n

print 'The first max: %s \nThe second max: %s' % (max_a,max_b)
