#encoding:utf -8

from  flask import Flask ,request,render_template,redirect,session
#import modes
#导入mysql模块
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
app.secret_key='asderwewrgtrryrtysfawewrerf@234342'
@app.route('/')
def index():
    if 'username' in session:
        return redirect('/user_list')
    return  render_template('login.html')
@app.route('/logout')
def logout():
    session.pop('username')
    return redirect('/')
@app.route('/login',methods=['POST','GET'])
def login():
    if 'POST' ==request.method:
        user = request.form.get('user')
        pwd = request.form.get('pwd')
    else:
        user = request.args.get('user')
        pwd = request.args.get('pwd')
    if user ==  '' and pwd == '':
        num_msg =  'user or pwd is empty'
    elif user == 'admin' and pwd =='admin':
        session['username'] ='admin'
        return  redirect('/user_list')
    else:
        num_msg = 'user or pwd is error'
    return render_template('login.html',num_msg = num_msg)
@app.route('/user_list')
def user_list():
    if 'username' in session:
#调用开头生成的元组用户列表
        users = user_tu()

        return render_template('user_list.html', user_list = users)
    else:
        return redirect('/')
@app.route('/user_sec',methods=['POST','GET'])
def user_sec():
    if 'GET' == request.method:
        sec_user = request.args.get('sec_user')
    else:
        sec_user = request.form.get('sec_user')
    num_msg =''
    sql = 'select user,pwd from user_list where user = "%s"'%sec_user
    cur.execute(sql)
    users = cur.fetchall()

    if sec_user =='':
        num_msg = 'please input user name'
    elif users ==():
        num_msg = "user is not exited"
    return render_template('user_list.html',user_list=users,num_msg=num_msg)
@app.route('/user_add',methods =['POST','GET'])
def user_add():
    if 'GET' == request.method:
        user = request.args.get('user')
        pwd = request.args.get('pwd')
    else:
        user = request.form.get('user')
        pwd = request.form.get('pwd')

    sql = 'insert into user_list values("%s","%s")'%(user,pwd)
    if user  in dict(user_tu()):
        num_msg = 'user is exited'
    elif not user :
        num_msg = 'user is empty'
    else:
        cur.execute(sql)
        return  redirect('/user_list')
    return render_template('user_list.html', num_msg = num_msg,user_list=user_tu())
@app.route('/user_modifys')
def user_modifys():
    user = request.args.get('user')
    pwd = request.args.get('pwd')
    return  render_template('user_modify.html',user = user,pwd=pwd)
@app.route('/user_modify',methods =['POST','GET'])
def user_modify():
    if 'GET' == request.method:
        new_pwd = request.args.get('new_pwd')
        user = request.args.get('user')
    else:
        new_pwd = request.form.get('new_pwd')
        user = request.form.get('user')
    sql = 'update  user_list set pwd = "%s" where user = "%s"'%(new_pwd,user)
    cur.execute(sql)
    return redirect('/user_list')
@app.route('/user_del')
def user_del():
    user = request.args.get('user')
    sql = 'delete from user_list where user = "%s"'%user
    cur.execute(sql)
    return redirect('/user_list')

@app.route('/ajax')
def ajax():
    return render_template("ajax.html")
@app.route('/usermore')
def usermore():
    return "xiao ning"

if __name__ == '__main__':
    app.run(host = '0.0.0.0',port=10001,debug=True)