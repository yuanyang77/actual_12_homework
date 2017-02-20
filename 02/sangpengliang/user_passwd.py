#encoding=utf-8

f = open('info.txt','r')
arr = f.read().split('\n')
f.close( )
name = raw_input("请输入用户名或手机号:")
pwd = raw_input("请输入密码:")

phone_list = []
user_list = []
pwd_list = []

for login in arr:
    temp = login.split(':')

    user_list.append(temp[0])
    phone_list.append(temp[1])
    pwd_list.append(temp[2])
    if name in phone_list or name in user_list:
        if pwd in pwd_list:
            print '登陆成功!'
        else:
            print '密码错误!'
        break
if not user_list or phone_list:
    print '用户不存在,请输入正确的用户名以及密码'

#arr = ['user:pwd','user1:pwd1','user2,pwd2']
#user = 'user33'
#pwd = 'pwd1'
#user_exists = False
#for u in arr:
#    temp = u.split(':')
#    if temp[0] == user:
#        if temp[1] == pwd:
#            msg = 'success'
#
#        else:
#            msg = 'wrong pwd'
#        user_exists = True
#        print msg
#        break
#if not user_exists:
#    print 'user not exists'