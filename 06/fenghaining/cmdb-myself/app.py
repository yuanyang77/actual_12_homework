#encoding: utf-8
from flask import Flask,redirect,request,render_template,url_for,flash,session
import models

app = Flask(__name__)
app.secret_key = '\xf4\xf7\x84\xe4\xf3\x84\x8bm\xb4Xe\xf3\x8d\xfa:\xce\xfbQ\xa9L\xe7x\x94}'

@app.route('/')
def index():
    # return render_template('index.html')
    if session.get('user'): return  redirect('/users/')
    # return redirect('/login/')
    # return redirect('/login/')
    return render_template('index.html')

@app.route('/login/',methods=['post','get'])
def login():
    if session.get('user'): return redirect('/users/')
    if request.method == 'POST':
        username = request.form.get('username','')
        password = request.form.get('password','')
    else:
        username = request.args.get('usrenmae','')
        password = request.args.get('password','')
    user = models.validate_login(username,password)
    print user
    if user:
        session['user'] = user
        return redirect('/users/')
    else:
        return render_template('index.html',username=username,password=password,error='username or password is error')



@app.route('/users/')
def users():
    if session.get('user') is None:return redirect('/')
    users = models.get_users()
    return render_template('users.html',users=users)

@app.route('/user/create/')
def user_create():
    if session.get('user') is None:return redirect('/')
    return render_template('user_create.html')

@app.route('/user/save/',methods=['post'])
def user_save():
    if session.get('user') is None:return redirect('/')
    username = request.form.get('username','')
    age = request.form.get('age','')
    password = request.form.get('password','')
    ok,error = models.validate_user_save(username,age,password)
    if ok:
        models.user_save(username,age,password)
        return redirect('/users/')
    else:
        return render_template('user_create.html',username=username,age=age,password=password,error=error)

@app.route('/user/view/')
def user_view():
    if session.get('user') is None:return redirect('/')
    id = request.args.get('id','')
    user = models.get_user_by_id(id)
    return render_template('user_view.html',id=user.get('id',''),name=user.get('name',''),age=user.get('age',''))


@app.route('/user/modify/',methods=['POST'])
def user_modify():
    if session.get('user') is None:return redirect('/')
    uid = request.form.get('id','')
    username = request.form.get('username','')
    age = request.form.get('age','')
    ok,error = models.validate_user_modify(uid,username,age)
    if ok:
        models.user_modify(uid,username,age)
        return redirect('/users/')
    else:
        return render_template('user_view.html',id=uid,name=username,age=age,error=error)



@app.route('/user/del/')
def user_del():
    if session.get('user') is None:return redirect('/')
    uid = request.args.get('id','')
    models.user_del(uid)
    return redirect('/users/')

@app.route('/logout/')
def logout():
    session.clear()
    return redirect('/')

@app.route('/select/')
def select():
    if session.get('user') is None:return redirect('/')
    username = request.args.get('username','').strip()
    users = models.select_users(username)
    # return redirect('/users/')
    return render_template('users.html',users=users,username=username)













@app.route('/log/')
def log():
    if session.get('user') is None:return redirect('/')
    topn =  request.args.get('topn')
    topn = int(topn) if str(topn).isdigit() else 10
    access_file_path = 'D:\\reboot\\www_access_20140823.log'
    result = models.get_top(access_file_path,topn)
    # for line in result:
    #     print line
    return render_template('log.html',logs = result)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80,debug=True)
