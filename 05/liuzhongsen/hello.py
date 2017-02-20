# coding=utf-8

# 作业 用户管理（基于文件存储）

# 1.管理员登陆（写死账号是admin 密码是pwd，不做也可以）
# 2.登陆之后 看到用户和密码列表（存储在文件中）支持添加，删除 的操作
# 3 选做 修改密码

from flask import Flask, redirect, request, render_template, url_for
import userm

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
    tmp = userm.is_admin(user=user, password=password)
    if tmp:
        return redirect('/usermanager')
    else:
        return render_template('login.html', error='Invalid username/password!')


# 用户列表
@app.route('/usermanager')
def usermanager():
    user_dict = userm.get_user()
    return render_template('usermanager.html', user_dict=user_dict)


# 跳转新增用户
@app.route('/usermanager/add')
def adduser():
    return render_template('add.html')


# 新增用户
@app.route('/usermanager/add', methods=['POST'])
def register():
    user = request.form.get('username')
    password = request.form.get('password')
    confimPassword = request.form.get('confimPassword')
    ok, error = userm.register(username=user, password=password, confimPassword=confimPassword)
    if ok:
        return redirect('/usermanager')
    return render_template('add.html', error=error)


# 跳转用户修改，并带入username
@app.route('/usermanager/modify')
def modify():
    username = request.args.get('username')
    return render_template('modify', username=username)


# 用户修改
@app.route('/usermanager/modify', methods = ['POST'])
def revise():
    username = request.args.get('username')
    password = request.args.get('password')
    confimPassword = request.args.get('confimPassword')
    ok, error = userm.revise_user(username=username, password=password, confimPassword=confimPassword)
    if ok:
        return redirect('/usermanager')
    return render_template('modify.html', username=username, error=error)


# 用户删除
@app.route('/usermanager/delete')
def delete():
    username = request.args.get('username')
    userm.delete_user(username=username)
    return redirect('/usermanager')


# 启动应用
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=9002, debug=True)
