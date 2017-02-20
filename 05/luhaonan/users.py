# coding=utf-8

# 是否管理员用户
def is_admin(user, password):
    if user == 'admin' and password == 'admin':
        return True
    return False

# 获取用户列表
def get_user():
    user_dict = {}
    with open('user.txt') as f:
        for i in f.readlines():
            username = i.split(':')[0].strip()
            password = i.split(':')[1].strip()
            user_dict[username] = password
    return user_dict

# 是否存在
def is_exist(username):
    if username in get_user():
        return False
    return True

# 写文件
def write_file(user):
    tmp = ''
    with open('user.txt', 'w') as f:
        for key, value in user.iteritems():
            tmp += '%s:%s\n' % (key, value)
        f.write(tmp)   

# 修改信息
def revise_user(username, password, confimPassword):
    if username == '' or password == '' or confimPassword == '':
        return False, 'username/password/confimPassword is empty!'
    elif password != confimPassword:
        return False, 'Two passwords are not consistent'
    users = get_user()
    for user in users:
        if user == username:
            users[user] = password
            break
    write_file(users)
    return True, ''

# 注册用户
def register(username, password, confimPassword):
    if username == '' or password == '' or confimPassword == '':
        return False, 'username/password/confimPassword is empty!'
    elif password != confimPassword:
        return False, 'Two passwords are not consistent'
    elif [i for i in get_user() if i == username]:
        return False, 'username is exist!'

    with open('user.txt', 'a') as f:
        tmp = '%s:%s\n' % (username, password)
        f.write(tmp)
    return True, ''

# 删除用户
def delete_user(username):
    users = get_user()
    tmp = ''
    for key in users:
        if key == username:
            del users[key]
            break
    write_file(users)


if __name__ == '__main__':
    print revise_user('qqq','333')
