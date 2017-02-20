#encoding:utf -8

from  flask import Flask ,request,render_template,redirect,session
import modes

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
@app.route('/login', methods =['POST','GET'])
def login():
    if 'GET' == request.method:
        user = request.args.get('user')
        pwd = request.args.get('pwd')
    else:
        user = request.form.get('user')
        pwd = request.form.get('pwd')
    num_msg=modes.user_login(user,pwd)
    if not num_msg:
        session['username'] ='admin'
        return  redirect('/user_list')
    return render_template('login.html',num_msg = num_msg)
@app.route('/user_list')
def user_list():
    if 'username' in session:
#调用开头生成的元组用户列表
        users = modes.user_list()
        if users:
            return render_template('user_list.html', user_list = users)
    else:
        return redirect('/')
@app.route('/user_sec',methods = ['POST','GET'])
def user_sec():
    if 'GET'==request.method:
        sec_user = request.args.get('sec_user')
    else:
        sec_user = request.form.get('sec_user')
    user = modes.user_sec(sec_user)
    return render_template('user_list.html',user_list=user[0],num_msg=user[1])
@app.route('/user_add',methods=['POST','GET'])
def user_add():
    if 'GET'==request.method:
        user = request.args.get('user')
        pwd = request.args.get('pwd')
    else:
        user = request.form.get('user')
        pwd = request.form.get('pwd')
    num_msg = modes.user_add(user,pwd)
    if not num_msg:
        return  redirect('/user_list')
    return render_template('user_list.html', num_msg = num_msg,user_list=modes.user_list())
@app.route('/user_modifys')
def user_modifys():
    user = request.args.get('user')
    pwd = request.args.get('pwd')
    return  render_template('user_modify.html',user = user,pwd=pwd)
@app.route('/user_modify',methods=['POST','GET'])
def user_modify():
    if 'GET' == request.method:
        new_pwd = request.args.get('new_pwd')
        user = request.args.get('user')
    else:
        new_pwd = request.form.get('new_pwd')
        user = request.form.get('user')
    modes.user_modify(user,new_pwd)
    return redirect('/user_list')
@app.route('/user_del',methods=['POST','GET'])
def user_del():
    if 'GET' == request.method:
        user = request.args.get('user')
    else:
        user = request.form.get('user')
    modes.user_del(user)
    return redirect('/user_list')

if __name__ == '__main__':
    app.run(host = '0.0.0.0',port=10001,debug=True)