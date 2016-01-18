# encoding:utf-8
from flask import Flask, render_template, redirect, request, json, url_for
from openxl import *
# from db import *
import time
ISOTIMEFORMAT = '%Y-%m-%d %X'
app = Flask(__name__)
app.debug = True


# 主页路由
@app.route('/', methods=['POST', 'GET'])
@app.route('/index')
def index():
    if request.method == 'POST':
        task = request.form.to_dict(flat=False)
        task_id = task["task_id"]
        table_message = "59146.xls"
        package = openxl(table_message)
        print "task_id:", task_id
        return render_template('show.html', package=package)
    else:
        return render_template('welcome.html')

# 用于呈现的路由


@app.route('/show', methods=['POST', 'GET'])
@app.route('/show/<table_message>', methods=['POST', 'GET'])
def show(table_message="target/59146.xls"):
    package = openxl(table_message)
    return render_template('show.html', package=package)

# post的地址，提供映射的方法


@app.route('/map', methods=['POST', 'GET'])
def map():
    status = "failed!"
    if request.method == 'POST':
        cur, conn = init_database()
        log = open('target/sql_log.txt', 'a')
        data = request.form.to_dict(flat=False)
        print len(data["master_id[]"])
        for i in range(0, len(data["master_id[]"])):
            print i + 1, data["master_id[]"][i], data["slave_id[]"][i]
            sql = "insert into drug_mapper (target,matched) values(%s,%s)" % (
                data["master_id[]"][i], data["slave_id[]"][i])
            cur.execute(sql)
            print "执行：" + sql
            conn.commit()
            print u"执行成功"
            # 写入日志前一定要字符串化信息
            string = sql + "$" + \
                time.strftime(ISOTIMEFORMAT, time.localtime()) + "\n"
            log.write(string)
        cur.close()
        conn.close()
        print u"断开数据库连接！"
        log.close()
        status = "success"
        return json.dumps(status)

if __name__ == '__main__':
    app.run(port=8080)
