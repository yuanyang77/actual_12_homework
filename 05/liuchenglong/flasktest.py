#encoding=utf-8
from flask import Flask,render_template,request
#实例化对象 app ，参数为应用模块或包的名称，这里 __name__ 指的是 __main__ 主程序。
# 这个参数是必需的，这样  Flask  就可以知道在哪里找到模板和静态文件等东西
app = Flask(__name__)

#使用 route() 装饰器告诉 Flask 触发函数的 URL 。
# 可以自定义,如 @app.route("/test1.py")，访问时则后面要接文件名
@app.route('/')
@app.route('/index')
def hello_world():
    return render_template('index.html')

@app.route('/login')
def loginpage():
    user = request.args.get('user')
    pwd = request.args.get('pwd')
    if user == 'admin' and pwd == 'pwd':
        with open('userlist.txt','r') as f:
            user_dict={}
            for line in f:
                temp = line.split(':')
                user_dict[temp[0]] = temp[1]

        return render_template('login.html',user_dict=user_dict)
    else:
        return 'login failed'
@app.route('/insert')
def insert():
    return render_template('insert.html')
@app.route('/add')
def add():
    user = request.args.get('user')
    pwd = request.args.get('pwd')
    with open('userlist.txt', 'a+') as f:
        f.write(user+":"+pwd+'\n')
    return "User insert Successful"+'<br>'+'<a href="/login?user=admin&pwd=pwd">Back</a>'
@app.route('/delete')
def delete():
    user = request.args.get('user')
    user_dict = {}
    with open('userlist.txt', 'r') as f:
        for line in f:
            temp = line.split(':')
            if temp[0]!= user:
                user_dict[temp[0]] = temp[1]
    with open('userlist.txt', 'w') as f:
        for user,pwd in user_dict.items():
            f.write( user+ ":" + pwd )

    return 'delete successful'+'<br>'+'<a href="/login?user=admin&pwd=pwd">Back</a>'


if __name__ == '__main__':
    app.run(debug=True)
#运行服务器应用，运行后默认只有本地可以访问，如需让其他连接，可以指定 host ，
# 如： app.run(host='0.0.0.0')默认使用的端口是： 5000 ，可以使用自定义的主机和端口：
#  app.run(host="0.0.0.0",port=8000)