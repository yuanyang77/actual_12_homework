#encoding:utf -8
#导入mysql模块
import MySQLdb  as mysql
#连接数据库返回链接对象
conn = mysql.connect(user='root',passwd='123456',host='127.0.0.1',db='jcm')
#刷新数据库
conn.autocommit(True)
 #获取游标对象，操作sql用
cur = conn.cursor()

def user_login(user='',pwd=''):
    if user =='' or pwd =='':
        num_msg='user or password is null'
    elif user=='admin' and pwd =='admin':
        num_msg=''
    else:
        num_msg ='user or password is error'
    return num_msg
def user_list():
    cur.execute('select * from user_list')
    users=cur.fetchall()
    return  users
def user_del(user=''):
    sql='delete  from user_list where user = "%s"' %user
    cur.execute(sql)
    cur.fetchall()
def user_add(user='',pwd=''):
    sql='insert into user_list values("%s","%s")'%(user,pwd)
    num_msg =''
    if user =='':
        num_msg = 'please input your name'
    elif user in dict(user_list()):
        num_msg = 'User is already exist'
    else:
        cur.execute(sql)
        cur.fetchall()
    return num_msg
def user_modify(user='',pwd=''):
    sql='update user_list set pwd ="%s" where user ="%s" '%(pwd,user)
    cur.execute(sql)
    cur.fetchall()
def user_sec(user=''):
    sql='select user,pwd from user_list where user ="%s"'%user
    cur.execute(sql)
    users=cur.fetchall()
    num_msg =''
    if user =='':
        num_msg = 'please input your name'
    elif users ==():
        num_msg ='user is not exist'
    return users,num_msg

#user_dict = {}
#def user_list():
#    with open('user.txt','r') as f:
#        for user in f.read().split('\n'):
#            temp = user.split(':')
#            if user:
#                user_dict[temp[0]]= temp[1]
#    return user_dict

#def user_write():
#    file_arr = []
#    for user,pwd in user_dict.items():
#        file_arr.append('%s:%s'%(user,pwd))
#    with open('user.txt','w') as f:
#        f.write('\n'.join(file_arr))
