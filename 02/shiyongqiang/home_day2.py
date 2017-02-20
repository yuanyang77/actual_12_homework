#!/usr/bin/python
#-coding:utf-8-
#Method 1:
f = open('user.txt')
arr = f.read().split('\n')
f.close()
_list = arr[0:3]
print _list

user=raw_input('Enter account: ') 
phone=raw_input('Enter phone number: ')
pwd=raw_input('Input password: ')

for i in _list: 
    if user == i.split(':')[1] or phone == i.split(':')[0]:
    if pwd == i.split(':')[2]:
        print "Login success"
        break
    else:
        print "Password error"
        break
    else:
    print "Account does not exist"
    break


#Method 2:
#第二种方法在linux执行会有报错，蜗牛大大求解
f = open('user.txt')
arr = f.read().split('\n')
f.close()
print arr

phone='111'
user='user11'
pwd='pwd1'

phone_list=[]
user_list=[]
pwd_list=[]

for i in arr:
    temp = i.split(':')
    phone_list.append(temp[0])
    user_list.append(temp[1])
    pwd_list.append(temp[2])
if user in user_list:
    if pwd == pwd_list[user_list.index(user)]:
        print "Login success!"
    else:
        print "Password error!"
elif phone in phone_list:
    if pwd == pwd_list[phone_list.index(phone)]:
        print "Phone login!"
    else:
        print "Phone number login success!"

else:
        print "Login failed!"
