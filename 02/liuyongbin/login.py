#coding=utf8
#使用用户名和手机号登录  文件形式
inputuser=raw_input('input your username: ')
inputpas=raw_input('input your phone: ')
myinfo=inputuser+':'+inputpas
#print myinfo

user_pas_list=[]
pho_pas_list=[]

f=open('/root/lyb/02/passwd','r')
allinfo=f.read().split('\n')
f.close()

allinfo.pop()
for i in allinfo:
    photmp=i.split(':')[0]
    usertmp=i.split(':')[1]
    pastmp=i.split(':')[2]
    user_pas_list.append(photmp+':'+pastmp)
    pho_pas_list.append(usertmp+':'+pastmp)

#print user_pas_list
#print pho_pas_list

if myinfo in user_pas_list or myinfo in pho_pas_list:
    print 'welcome'
else:
    print 'wrong user or pas!!!'
