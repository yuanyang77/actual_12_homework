#encoding:utf -8
from flask import redirect

def login_user(user='',pwd =''):
    if user == 'admin' and pwd =='pwd':
        num_msg =None
    else:
        num_msg = 'username or password is error'
    return num_msg
def user_list():
    users = {}
    with open('user.txt','r') as f:
        user = f.read().split('\n')
        for u in user:
            if u == '':
                continue
            use = u.split(':')
            users[use[0]] = use[1]

    return  users
def user_del(user='',pwd=''):
    users = user_list()
    f = open('user.txt','w')
    f.close()
    for use in users:
        if user == use:
            continue
        else:
            with open('user.txt','a+') as f:
                f.write(''.join(use)+':'+''.join(users[use])+'\n')

def user_adds(user='',pwd=''):
    users = user_list()
    message = None
    if user == '':
        message = 'user  is empty'
    elif user in users:
        message = 'User already exists'
    else:
        with open('user.txt','a+')  as f:
            f.write(''.join(user)+':'+''.join(pwd)+'\n')
    return message
def user_modify(user='',pwd=''):
    users = user_list()
    message =None
    if user == ''and pwd =='':
        message = 'user or pwd is empty'
    elif user not in users:
        message = 'user does not exist'
    else:
        users[user] = pwd
        f = open('user.txt','w')
        f.close()
        for use in users:
            with open('user.txt','a+')  as f:
                f.write(''.join(use)+':'+''.join(users[use])+'\n')
    return message
