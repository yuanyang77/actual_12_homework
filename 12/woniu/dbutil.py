
import MySQLdb as ms


class DB:
    def __init__(self,host,user,passwd,db):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.db = db
        self.connect()
    def execute(self,sql):
        try:
            self.cursor.execute(sql)
        except Exception as e:
            self.conn.close()
            self.cursor.close()
            self.connect()
            return self.execute(sql)
        else:
            return self.cursor

    def connect(self):
        self.conn = ms.connect(host=self.host,user=self.user,passwd=self.passwd,db=self.db)
        self.conn.autocommit(True)
        self.cursor = self.conn.cursor()

db = DB(user='woniu',passwd='123456',host='59.110.12.72',db='woniu')
