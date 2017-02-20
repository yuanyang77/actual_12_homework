#!/usr/bin/env python
#coding=utf-8
import MySQLdb as mysql

def get_mysql():
    try:
        conn = mysql.connect(host="localhost",user="root",passwd="root",db="yubin",charset="utf8")
        conn.autocommit(True)
        return conn
    except:
        print "get mysql error"

def action(sql):
    try:
        con = get_mysql()
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()
    except mysql.Error as e:
        print 'mysql error %d %s'%(e.args[0],e.args[1])
    finally:
        cur.close()
        get_mysql().close()





