#!/usr/bin/env python
#coding=utf-8

def select_user():
    user_dict = {}
    with open('user.txt') as f:
        for line in f.read().split('\n'):
            if line:
                temp = line.split(':')
                user_dict[temp[0]] = temp[1]
                #user_dict.setdefault(temp[0],temp[1])
    return user_dict

def delete_user(user):
    user_dict = select_user()
    if user in user_dict:
        user_dict.pop(user)
    with open('user.txt','w') as ff:
        for k,v in user_dict.items():
            kv = '%s:%s\n' %(k,v)
            ff.write(kv)

def insert_user(user,pwd):
    with open('user.txt','a') as ff:
        #kv = user+':'+pwd+'\n'
        kv = '%s:%s\n' %(user,pwd)
        ff.write(kv)
