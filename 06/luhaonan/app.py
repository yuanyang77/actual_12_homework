# coding=utf-8

# 作业 用户管理（基于文件存储）

# 1.管理员登陆（写死账号是admin 密码是pwd，不做也可以）
# 2.登陆之后 看到用户和密码列表（存储在文件中）支持添加，删除 的操作
# 3 选做 修改密码

from flask import Flask, redirect, request, render_template, session
import users
import json
# import db
# conn = db(user='mysql', passwd='mysql', host='127.0.0.1', db='51reboot')
# import MySQLdb as mysql
# conn = mysql.connect(user='mysql', passwd='mysql', host='127.0.0.1', db='51reboot', charset="utf8")
# conn.autocommit(True)  # 设置事务自动提交,执行insert后不用 conn.commit()
# db = conn.cursor()
# db.execute('select * from user')
# print db.fetchall


# 新建app
app = Flask(__name__)

app.secret_key = 'ewuhksjdfbxmnv!&#^$*&@^#'

@app.route('/')
def index():
    if 'username' in session:
        return redirect('/userlist')
    return render_template('login.html')


# 登录页
@app.route('/login', methods=['POST', 'GET'])
def login():
    # error = None
    if 'POST' == request.method:
        data = request.form.to_dict()
    else:
        data = request.args.to_dict()
    tmp = users.is_admin(user=data['username'], password=data['password'])
    if tmp:
        session['username'] = 'admin'
        return redirect('/userlist')
    else:
        return render_template('login.html', error='Invalid username/password!')

# 退出登录
@app.route('/logout')
def logout():
    session.pop('username')
    return redirect('/')


# 用户列表
@app.route('/userlist')
def userlist():
    if 'username' in session:
        return render_template('list.html', users=users.get_user())
    else:
        return redirect('/')


# 新增用户
@app.route('/userlist/adduser', methods=['GET', 'POST'])
def adduser():
    if 'username' not in session:
        return redirect('/login')
    elif request.method == 'GET':
        return render_template('adduser.html')
    elif request.method == 'POST':
        data = request.form.to_dict()
        ok, msg = users.update_user(mode=0, username=data['username'], password=data['password'], confimPassword=data['confimPassword'])
        if ok:
            return redirect('/userlist')
        return render_template('adduser.html', error=msg)
    return render_template('adduser.html', error='你这个大坏淫!')


# 修改用户密码
@app.route('/userlist/revise', methods=['GET', 'POST'])
def modify():
    if 'username' not in session:
        return redirect('/login')
    elif request.method == 'GET':
        username = request.args.get('username')
        return render_template('revise.html', username=username)
    elif request.method == 'POST':
        data = request.form.to_dict()
        ok, msg = users.update_user(mode=1, username=data['username'], password=data['password'], confimPassword=data['confimPassword'])
        if ok:
            return redirect('/userlist')
        return render_template('revise.html', username=data['username'],error=msg)
    return render_template('adduser.html', error='你这个大坏淫!')


# 删除用户
@app.route('/userlist/delete')
def delete():
    user_id = request.args.get('id')
    ok = True#users.delete_user(user_id=user_id)
    if ok:
        return json.dumps({'code':'0', 'msg':'删除成功！'})
    return json.dumps({'code':'99', 'msg':'删除失败！'})


# 启动应用
if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)

