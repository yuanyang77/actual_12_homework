#encoding:utf-8
from flask import Flask ,render_template,request,redirect
import modes
app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')
@app.route('/login')
def login_user():
    user = request.args.get('user')
    pwd =  request.args.get('pwd')
    num_msg = modes.login_user(user,pwd)
    if num_msg==None:
        return redirect('/user')
    else:
        return  render_template('login.html',num_msg=num_msg)
@app.route('/user')
def user_list():
    users = modes.user_list()
    return render_template('user.html',user_list=users)
@app.route('/user_adds')
def user_adds():
    return render_template('add_user.html')
@app.route('/user_modify')
def user_modifys():
    user = request.args.get('user')
    pwd = request.args.get('pwd')
    return render_template('modify.html',user=user,pwd=pwd)
@app.route('/modify')
def user_modify():
    user = request.args.get('user')
    pwd = request.args.get('pwd')
    num_msg=modes.user_modify(user,pwd)
    if num_msg is None:
        return redirect('/user')
    else:
        return render_template('modify.html',user=user,pwd=pwd,num_msg=num_msg)
@app.route('/add')
def user_add():
    user = request.args.get('user')
    pwd = request.args.get('pwd')
    num_msg = modes.user_adds(user,pwd)
    if num_msg is None:
        return redirect('/user')
    else:
        return render_template('add_user.html',num_msg=num_msg)
@app.route('/del')
def user_del():
    user = request.args.get('user')
    modes.user_del(user)
    return redirect('/user')
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=10001,debug=True)
