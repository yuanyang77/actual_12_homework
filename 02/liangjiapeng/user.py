#!/bin/env python
#coding:utf8
#获取用户输入
input_user=raw_input("input_user:")
input_pass=raw_input("input_pass:")

#文件内容导入列表
username=[]
passwd=[]
f = open('./icbc.txt')
STXT = f.readlines()
for i in STXT:
    tmp=i.split(":")
    username.append([tmp[0],tmp[1]])
    passwd.append(tmp[2].split("\n")[0])


#用户登录判断
userstatus=False
for x in username:
    if input_user in x:
        if input_pass == passwd[username.index(x)]:
            print "user ok"
            userstatus=True
        else:
            print "pass err"
            userstatus=True
if not userstatus:
    print "user no"
f.close()
