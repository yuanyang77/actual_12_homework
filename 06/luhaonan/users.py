# coding=utf-8
import db
import datetime

# SELECT = 'SELECT ID,UserName,Mobile,role,Status,CreateTime FROM user'
# SELECT = 'SELECT ID,UserName,Status,CreateTime FROM user'
INSERT = "INSERT INTO user VALUES (NULL,'%s',NULL,'%s',NULL,'%s','%s',0,'%s',NULL)"
UPDATE = "UPDATE user SET PassWord='%s' WHERE UserName='%s'"
# DELETE = "DELETE FROM user WHERE ID='%s'"


# 是否管理员用户
def is_admin(user, password):
    if user == 'admin' and password == 'admin':
        return True
    return False


# 获取用户列表
def get_user():
    fields = ['ID', 'UserName', 'Status', 'CreateTime']
    sql = 'SELECT %s FROM user WHERE Status!=2' % ','.join(fields)
    result = db.query(sql=sql)
    u_list = [dict((k, row[i]) for i, k in enumerate(fields)) for row in result]
    return u_list


# mode=0注册用户, mode=1修改信息
def update_user(mode, username, password, confimPassword):
    # print mode,username,password,confimPassword
    if username == '' or password == '' or confimPassword == '':
        return False, 'username/password/confimPassword is empty!'
    elif password != confimPassword:
        return False, 'Two passwords are not consistent'
    elif mode == 1:
        db.update(UPDATE % (password, username))
        return True, ''
    elif [i for i in get_user() if username in i]:
        return False, 'username is exist!'
    elif mode == 0:
        db.update(INSERT % (username, password, '110', '0', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        return True, ''

# 改为使用update方式假删除
# 删除用户
def delete_user(user_id):
    if [i for i in get_user() if int(user_id) == i[0]]:
        db.update('UPDATE user WHERE Status = 2 WHERE ID=%s' % user_id)
        return True
    return False


if __name__ == '__main__':
    get_user()
