#!/usr/bin/python
# -*- coding:utf-8 -*-
f = open('user.txt')
s = f.read().split('\n')
f.close()
s.pop()
new_list = s[::]
print new_list

user=raw_input('please you user name:')
pwd=raw_input('please you password:')
user_exists=False

for i in new_list:
    temp = i.split(':')
    print temp
    if temp[0]==user or temp[1]==user:
        if temp[2]==pwd:
            user_exists = True
            print 'login user successful'
            break
        else:
            user_exist=True
            print 'ERROR: pwd is wrong'
            break
if not user_exists:
    print 'user ERROR'