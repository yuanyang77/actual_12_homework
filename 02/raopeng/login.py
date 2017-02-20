#coding=utf8
f = open('user')
arr = f.read().split('\n')
name_num = []
name_pwd = []
num_pwd = []
for i in arr:
	if i=="":
		continue
	else:
		temp = i.split(":")
		name_num.append(temp[0])
		name_num.append(temp[1])
		name_pwd.append(temp[1]+':'+temp[2])
		num_pwd.append(temp[0]+':'+temp[2])
user = raw_input('请输入手机号或用户名:')
if user not in name_num:
	print '输入的手机号或用户名不存在!!!'
else:
	count = 0
	while True:
		passwd = raw_input('请输入密码:')
		if user+':'+passwd not in name_pwd and user+':'+passwd not in num_pwd:
			count += 1
			print '输入的密码错误,还有%s次机会!!!' %(3-count)
			if count>=3:
				print '密码输错3次，不能登录!!!'
				break
		else:
			print '登录成功！'
			break
f.close()
