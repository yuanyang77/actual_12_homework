#encoding: utf -8
#读取文件use.txt 内有手机号，用户名，密码['1111',user,pwd1]
#手机号和用户名都可以登录
#测试有效用户名密码
f = open('user.txt')
arr =  f.read().split('\n')
f.close()

user = raw_input('please input you user name: ')
pwd = raw_input('please input you password: ')
shouji = raw_input('please input you Cell-phone number: ')
print ''
shouji_list = []
user_list = []
pwd_list = []
for  i in arr:
    temp = i.split(':')
    shouji_list.append(temp[0])
    user_list.append(temp[1])
    pwd_list.append(temp[2])
if user in user_list:
    if pwd == pwd_list[user_list.index(user)]:
        print "the name and password you input is right"
    else:
        print "you input password is error"
elif shouji in shouji_list:
    if pwd == pwd_list[shouji_list.index(shouji)]:
         print "The Cell-phone number and password you input is right"
else:
    print('The name or Cell-phone number  you input is Non-existent')