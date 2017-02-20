#coding=utf-8
f = open('test.txt')
arr = f.read().split('\n')
#以换行符进行分割
f.close
#打开并使用文件内的数据
arr_list = arr[:]
# print arr_list
tel = '189'
user = ''
pwd = '123'

tel_list = []
user_list = []
pwd_list = []

for i in arr_list:
	temp = i.split(':')
	tel_list.append(temp[0])
	user_list.append(temp[1])
	pwd_list.append(temp[2])
# print tel_list,user_list,pwd_list

if tel in tel_list:
    if pwd == pwd_list[tel_list.index(tel)]:
		    print "login success(tel)"
	  else:
		    print 'wrong password'

elif user in user_list:
    if pwd == pwd_list[user_list.index(user)]:
		    print 'login success(user)'
	  else:
		    print 'wrong password'
else:
	  print 'user not exists'

# 循环arr
# 	电话+':'+密码 正确
# 		用户名存在
# 		登录成功
# 	用户名+':'密码 正确
# 		用户名存在
# 		登录成功
# 	用户名存在 密码错误
# 		用户名存在
# 		密码错误
# 		break
# 如果用户和电话都不存在：
# 	登录失败
