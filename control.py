# encoding:utf-8
from flask import Flask, render_template, redirect, request, json
from openxl import *
from db import *
import time
ISOTIMEFORMAT='%Y-%m-%d %X'
app = Flask(__name__)
app.debug = True

#主页的路由
@app.route('/')
def index():
    package = openxl("target/ziyang20160111.xls")
    return render_template('index.html', package=package)

#post的地址，提供映射的方法
@app.route('/map', methods=['POST', 'GET'])
def map():
    status = "failed!"
    if request.method == 'POST':
        cur,conn = init_database()
        log = open('target/sql_log.txt','a')
        data = request.form.to_dict(flat=False)
        print len(data["master_id[]"])
        for i in range (0, len(data["master_id[]"])):
            print i+1,data["master_id[]"][i],data["slave_id[]"][i]
            sql = "insert into drug_mapper (target,matched) values(%s,%s)"%(data["master_id[]"][i],data["slave_id[]"][i])
            cur.execute(sql)
            print "执行："+sql
            conn.commit()
            print u"执行成功"
            # 写入日志前一定要字符串化信息
            string = sql+"$"+ time.strftime( ISOTIMEFORMAT, time.localtime() )+"\n"
            log.write(string)
        cur.close()
        conn.close()
        print u"断开数据库连接！"
        log.close()
        status = "success"
        return json.dumps(status)

if __name__ == '__main__':
    app.run(port=8080)
