# coding=utf-8

# 作业 用户管理（基于文件存储）

# 1.管理员登陆（写死账号是admin 密码是pwd，不做也可以）
# 2.登陆之后 看到用户和密码列表（存储在文件中）支持添加，删除 的操作
# 3 选做 修改密码

from flask import Flask, redirect, request, render_template, url_for
import users

# 新建app
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('login.html')


# 登录页
@app.route('/login', methods=['POST', 'GET'])
def login():
    # error = None
    if 'POST' == request.method:
        user = request.form.get('username')
        password = request.form.get('password')
    else:
        user = request.args.get('username')
        password = request.args.get('password')
    tmp = users.is_admin(user=user, password=password)
    if tmp:
        return redirect('/userlist')
    else:
        return render_template('login.html', error='Invalid username/password!')


# 用户列表
@app.route('/userlist')
def userlist():
    user_dict = users.get_user()
    return render_template('list.html', user_dict=user_dict)


# 跳转新增用户
@app.route('/userlist/adduser')
def adduser():
    return render_template('register.html')


# 新增用户
@app.route('/userlist/register', methods=['POST'])
def register():
    user = request.form.get('username')
    password = request.form.get('password')
    confimPassword = request.form.get('confimPassword')
    ok, error = users.register(username=user, password=password, confimPassword=confimPassword)
    if ok:
        return redirect('/userlist')
    return render_template('register.html', error=error)


# 跳转用户修改，并带入username
@app.route('/userlist/modify')
def modify():
    username = request.args.get('username')
    return render_template('revise.html', username=username)


# 用户修改
@app.route('/userlist/revise', methods = ['POST'])
def revise():
    username = request.args.get('username')
    password = request.args.get('password')
    confimPassword = request.args.get('confimPassword')
    ok, error = users.revise_user(username=username, password=password, confimPassword=confimPassword)
    if ok:
        return redirect('/userlist')
    return render_template('revise.html', username=username, error=error)


# 用户删除
@app.route('/userlist/delete')
def delete():
    username = request.args.get('username')
    users.delete_user(username=username)
    return redirect('/userlist')


# 启动应用
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
