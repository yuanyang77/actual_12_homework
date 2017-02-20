#coding=utf-8

f = open('user.txt')
arr = f.read().split('\n')
f.close()

input_user = '222'
input_pwd = 'pwd1'

user_exists = False
for i in arr:
    temp = i.split(':')
    if temp[1] == input_user or temp[0] == input_user:
        if temp[2] == input_pwd:
            msg = 'login success!'
        else:
            msg = 'pwd error!'
        user_exists = True
        print msg
        break
if not user_exists:
    print 'no user exists!'