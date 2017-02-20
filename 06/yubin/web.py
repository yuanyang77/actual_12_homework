#coding=utf-8
from flask import Flask,render_template,request,redirect,session
import data

app = Flask(__name__)
app.secret_key = '123qweasdqweq12efwrssarwevdvfdgrdwe'
@app.route('/')
def index():
    if 'username' in session:
        return redirect('/list')
    return render_template('login.html')
@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        user = request.form.get('user')
        pwd = request.form.get('pwd')
        if user == 'admin' and pwd == 'admin':
            session['username'] = user
            return redirect('/list')
        return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username')
    return redirect('/')

@app.route('/list')
def userlist():
    userlist = data.action('select * from user')
    if 'username' in session:
        return render_template('list.html',userlist=userlist)
    else:
        return redirect('/')
@app.route('/del')
def del_user():
    user = request.args.get('user')
    data.action('delete from user where name = "%s"'%user)
    return redirect('/list')

@app.route('/adduser')
def adduser():
    user = request.args.get('user')
    pwd = request.args.get('pwd')
    data.action('insert into user values ("%s","%s")'%(user,pwd))
    return redirect('/list')
@app.route('/update')
def update():
    user = request.args.get('user')
    pwd = data.action('select password from user where name="%s"'%user)
    return render_template('update.html',user=user,pwd=pwd[0][0])
@app.route('/updateaction')
def updateaction():
    user = request.args.get('user')
    pwd = request.args.get('new_pwd')
    data.action('update user set password="%s" where name = "%s"'%(pwd,user))
    return redirect('/list')

if __name__=='__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)