from flask import Flask,render_template
from dbutil import db
import json
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('echarts.html')
@app.route('/bar')
def bar():
    return render_template('echarts_bar.html')
@app.route('/map')
def map():
    return render_template('echarts_map.html')
@app.route('/mapdata')
def mapdata():
    sql = 'select * from log_map '
    cur = db.execute(sql)
    res = {
        'data':[],
        'geoCoordMap':{}
    }
    for l in cur.fetchall():
        ip = l[1]
        x = l[2]
        y = l[3]
        count = l[5]
        res['data'].append({
            'name':ip,
            'value':count
        })
        res['geoCoordMap'][ip] = [x,y]

    return json.dumps(res)


@app.route('/piedata')
def piedata():
    sql = 'select status,sum(count) from log group by status'
    cur = db.execute(sql)
    res = {
        'legend':[],
        'data':[]
    }
    for c in cur.fetchall():
        code = c[0]
        count = int(c[1])
        res['legend'].append(code)
        res['data'].append({
            'name':code,
            'value':count
        })
    return json.dumps(res)



if __name__=='__main__':
    app.run(host='0.0.0.0',port=9092,debug=True)
