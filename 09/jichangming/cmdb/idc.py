#encoding:utf -8

from  flask import Flask ,request,render_template,redirect,session
#import modes
#导入mysql模块
import json
import MySQLdb as mysql
#连接数据库返回链接对象
conn = mysql.connect(user='root',passwd='123456',host='127.0.0.1',db='jcm')
#刷新数据库
conn.autocommit(True)
 #获取游标对象，操作sql用
cur = conn.cursor()
#先查询所有用户列表，生成元组列表user_tuple,以备之后调用
def user_tu():
    cur.execute('select * from user_list')
    user_tuple = cur.fetchall()
    return user_tuple
app = Flask(__name__)

@app.route('/')
def index():
    return  render_template('index.html')
@app.route('/machine')
def machine():
    return render_template('machine.html')
@app.route('/idclist')
def idclist():
    cur.execute('select * from idc')
    res = cur.fetchall()
    return json.dumps(res)
@app.route('/addidc',methods=["post"])
def addidc():
    idc_name=request.form.get('name')
    sql = 'insert into idc(name) values ("%s")'%(idc_name)
    cur.execute(sql)
    return 'ok'
@app.route('/machinelist')
def machinelist():
    cur.execute('select * from pc')
    pc = cur.fetchall()
    return json.dumps(pc)
@app.route('/addmachine',methods=["post"])
def addmachine():
    ip=request.form.get('ip')
    mem=request.form.get('mem')
    idc_id=request.form.get('idc_id')
    create_time=request.form.get('create_time')
    sql = 'insert into pc(ip,mem,idc_id,create_time) values( "%s","%s","%s","%s")'%(ip,mem,idc_id,create_time)
    cur.execute(sql)
    return "ok"
@app.route('/delpc',methods=["post"])
def delpc():
    id = request.form.get('id')
    sql = 'delete from pc where id = %s'%id
    cur.execute(sql)
    return "ok"
@app.route('/modifypc',methods=["post"])
def modifypc():
    id = request.form.get('id')
    ip = request.form.get('ip')
    mem = request.form.get('mem')
    idc_id = request.form.get('idc_id')
    create_time = request.form.get('create_time')
    sql = 'update pc set ip = "%s", mem = "%s" ,idc_id ="%s",create_time="%s"  where id ="%s"'%(ip,mem,idc_id,create_time,id)
    cur.execute(sql)
    return "ok"
if __name__ == '__main__':
    app.run(host = '0.0.0.0',port=10001,debug=True)