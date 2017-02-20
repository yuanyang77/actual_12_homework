#encoding: utf-8
#打开文件
f=file("user.txt")
arr=f.read().split("\n")
print "arr的数组为：%s" %(arr)

#定义登录次数
count=0
#定义下数组
num_name=[]
num_pwd=[]
num_shouji=[]

#遍历添加到数组
for i in arr:
    if i == '':
        continue
    temp=i.split(":")
    num_shouji.append(temp[0])
    num_name.append(temp[1])
    num_pwd.append(temp[2])

print "num_shouji:%s,num_name:%s,num_pwd:%s" %(num_shouji,num_name,num_pwd)

#用户输入名字，密码，手机号
name=raw_input("输入用户名：")
shouji=raw_input("输入手机号：")

while True:
    pwd=raw_input("输入密码：")
    if name in num_name:
        if pwd == num_pwd[num_name.index(name)]:
            print "用户名，密码登录成功"
            break

    elif shouji in num_shouji:
        if pwd == num_pwd[num_shouji.index(shouji)]:
            print "手机号，密码登录成功"
    elif pwd not in num_pwd:
            print "登录失败"
            count+=1
            print "登录失败,还剩下%s次" %(3-count)
            if count >= 3:
                print "登录超过3次，退出"
                break
f.close()
