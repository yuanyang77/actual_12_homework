# coding:utf-8

import MySQLdb


def get_conn():
    try:
        conn = MySQLdb.connect(user='mysql', passwd='mysql', host='127.0.0.1', db='51reboot', charset="utf8")
        return conn
    except MySQLdb.Error as e:
        print 'Mysql Error %d: %s' % (e.args[0], e.args[1])


def query(sql):
    try:
        con = get_conn()
        cur = con.cursor()
        cur.execute(sql)
        data = cur.fetchall()
        return data
    except MySQLdb.Error as e:
        print 'Mysql Error %d: %s' % (e.args[0], e.args[1])
    finally:
        cur.close()
        con.close()


def update(sql):
    try:
        con = get_conn()
        cur = con.cursor()
        cur.execute(sql)
        con.commit()
    except MySQLdb.Error as e:
        con.rollback()
        print 'Mysql Error %d: %s' % (e.args[0], e.args[1])
    finally:
        cur.close()
        con.close()


if __name__ == '__main__':
    pass