#encoding: utf-8
import json
import MySQLdb as sql
import gconf

def get_top(src,top=10):
    stat_dict = {}
    with open(src,'rb') as f:
        # print f
        for line in f:
            if line == '\n':continue
            line_list = line.split()
            # print line_list
            key = (line_list[0],line_list[6],line_list[8])
            stat_dict[key] = stat_dict.setdefault(key,0) + 1
    result = sorted(stat_dict.items(),key=lambda x:x[1])
    return result[:-top-1:-1]

def validate_login(username,password):
    conn = sql.connect(host=gconf.MYSQL_HOST,\
                   port=gconf.MYSQL_PORT,\
                   user=gconf.MYSQL_USER,\
                   passwd=gconf.MYSQL_PASSWD,\
                   db=gconf.MYSQL_DB,\
                   charset=gconf.MYSQL_CHARSET)
    # print conn
    cur = conn.cursor()
    cnt = cur.execute('select id,name from user where name=%s and password=%s',(username,password))
    rt = cur.fetchone()
    cur.close()
    conn.close()
    print rt
    # print dict(zip(('id','username'),rt))
    return None if rt is None else dict(zip(('id','username'),rt))



def get_users():
    conn = sql.connect(host=gconf.MYSQL_HOST,\
                       port=gconf.MYSQL_PORT,\
                       user=gconf.MYSQL_USER,\
                       passwd=gconf.MYSQL_PASSWD,\
                       db=gconf.MYSQL_DB,\
                       charset=gconf.MYSQL_CHARSET)
    # print conn
    cur = conn.cursor()
    cur.execute('select id,name,age,password from user')
    rt_list = cur.fetchall()
    cur.close()
    conn.close()
    # print [dict(zip(('id','name','age'),line)) for line in rt_list]
    # print [dict(zip(('id','name','age'),line)) for line in rt_list]
    # for line in rt_list:
    #     print line
    return [dict(zip(('id','name','age','password'),line)) for line in rt_list]

    '''
    fh=open('user.json','rb')
    users = json.loads(fh.read())
    # users = fh.read()
    fh.close()
    return users
    '''

def select_users(username):
    conn = sql.connect(host=gconf.MYSQL_HOST,\
                       port=gconf.MYSQL_PORT,\
                       user=gconf.MYSQL_USER,\
                       passwd=gconf.MYSQL_PASSWD,\
                       db=gconf.MYSQL_DB,\
                       charset=gconf.MYSQL_CHARSET)
    # print conn
    cur = conn.cursor()
    cur.execute('select id,name,age,password from user where name=%s',(username,))
    rt_list = cur.fetchall()
    cur.close()
    conn.close()
    # print [dict(zip(('id','name','age'),line)) for line in rt_list]
    # print [dict(zip(('id','name','age'),line)) for line in rt_list]
    # for line in rt_list:
    #     print line
    return [dict(zip(('id','name','age','password'),line)) for line in rt_list]


def save_users(users):
    fh = open('user.json','wb')
    fh.write(json.dumps(users))
    fh.close()
    return True


def validate_user_save(username,age,password):
    users = get_users()
    if username.strip() == '':
        return False,'username is empty'
    if len(username.strip()) > 25:
        return False,'username must be lt 25'
    if password.strip() == '':
        return False,'password is empty'
    if len(password.strip()) > 25 or len(password.strip()) <6:
        return False,'password len is between 6 and 25'
    for user in users:
        if user.get('username') == username:
            return False,'username is exits'
    if not str(age).isdigit() or int(age) >100 or int(age) <1:
        return False,'age must be between 0 and 100'

    return True,''

def user_save(username,age,password):
    conn = sql.connect(host=gconf.MYSQL_HOST,\
                       port=gconf.MYSQL_PORT,\
                       user=gconf.MYSQL_USER,\
                       passwd=gconf.MYSQL_PASSWD,\
                       db=gconf.MYSQL_DB,\
                       charset=gconf.MYSQL_CHARSET)
    cur=conn.cursor()
    cnt = cur.execute('insert into user(name,age,password) values(%s,%s,%s)',(username,age,password))
    conn.commit()
    cur.close()
    conn.close()
    return cnt != 0



    '''
# def user_save():
    users = get_users()
    # print users
    # for line in users:
    #     print line
    users_sorted = sorted(users,key=lambda x:x['id'],reverse=True)
    # print users_sorted
    # for line  in users_sorted:
    #      print line
    id = users_sorted[0]['id'] + 1
    user = {'id':id,'username':username,'age':age,'password':password}
    users.append(user)
    return save_users(users)
    '''

def user_del(uid):
    conn = sql.connect(host=gconf.MYSQL_HOST,\
                       port=gconf.MYSQL_PORT,\
                       user=gconf.MYSQL_USER,\
                       passwd=gconf.MYSQL_PASSWD,\
                       db=gconf.MYSQL_DB,\
                       charset=gconf.MYSQL_CHARSET)
    cur=conn.cursor()
    cnt = cur.execute('delete from user where id=%s',(uid))
    conn.commit()
    cur.close()
    conn.close()
    return cnt != 0



    '''
# def user_del():
    users = get_users()
    print users
    # for user in users:
    #     print user
    for user in users:
        if uid == user['id']:
            users.remove(user)
    return save_users(users)
    '''


def get_user_by_id(uid):
    conn = sql.connect(host=gconf.MYSQL_HOST,\
                       port=gconf.MYSQL_PORT,\
                       user=gconf.MYSQL_USER,\
                       passwd=gconf.MYSQL_PASSWD,\
                       db=gconf.MYSQL_DB,\
                       charset=gconf.MYSQL_CHARSET)
    cur=conn.cursor()
    cnt = cur.execute('select id,name,age from user where id=%s',(uid,))
    rt= cur.fetchone()
    cur.close()
    conn.close()
    print rt
    # print  dict(zip(('id','name','age'),rt))
    return {} if rt is None else dict(zip(('id','name','age'),rt))

def validate_user_modify(uid,username,age):
    if username.strip() == '':
        return False,'username is empty'
    if len(username.strip()) > 25:
        return False,'username lenis not gt 25'
    if not str(age).isdigit() or int(age) < 1 or int(age) >100:
        return False,'age must be between 0 and 100'
    conn=sql.connect(host=gconf.MYSQL_HOST, \
           port=gconf.MYSQL_PORT, \
           user=gconf.MYSQL_USER, \
           passwd=gconf.MYSQL_PASSWD, \
           db=gconf.MYSQL_DB, \
           charset=gconf.MYSQL_CHARSET)
    #print conn
    cur=conn.cursor()
    cnt = cur.execute('select id from user where id != %s and name=%s',(uid,username.strip()))
    # rt = cur.fetchall()
    cur.close()
    conn.close()
    if cnt != 0:
        return False,'username is same to other'
    return True,''

def user_modify(uid,username,age):
    conn=sql.connect(host=gconf.MYSQL_HOST, \
                   port=gconf.MYSQL_PORT, \
                   user=gconf.MYSQL_USER, \
                   passwd=gconf.MYSQL_PASSWD, \
                   db=gconf.MYSQL_DB, \
                   charset=gconf.MYSQL_CHARSET)
    #print conn
    cur = conn.cursor()
    cnt = cur.execute('update user set name=%s,age=%s where id=%s',(username,age,uid))
    conn.commit()
    cur.close()
    conn.close()
    return True



if __name__ == '__main__':
    # get_users()
    get_user_by_id(1)