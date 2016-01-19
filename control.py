# encoding:utf-8
from flask import Flask, render_template, redirect, request, json, url_for
from openxl import *
from db import *
import time
from wtforms import Form, TextField, validators
from flask.ext.sqlalchemy import SQLAlchemy

ISOTIMEFORMAT = '%Y-%m-%d %X'
app = Flask(__name__)
# app.debug = True
app.debug = False
database = SQLAlchemy(app)
app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'mysql://root:%s@127.0.0.1/mapper' % ('toor')


class session_task(database.Model):
    __tablename__ = 'task'
    task_id = database.Column(database.Integer, primary_key=True)
    middle_result_name = database.Column(database.String(200))
    student_num = database.Column(database.Integer)
    student_name = database.Column(database.String(50))


class form_id(Form):
    task_id = TextField("task_id", [validators.Required()])

# 主页路由


@app.route('/', methods=['POST', 'GET'])
@app.route('/index')
def index():
    task_form = form_id(request.form)
    if request.method == 'POST':
        task_id = task_form.task_id.data
        # cur, conn = init_database('127.0.0.1', 'root', 'toor', 'mapper')
        # sql = "select middle_result_name from task where task_id = %s" % task_id
        # cur.execute(sql)
        # table_message = cur.fetchone()
        # print str(table_message)
        task = session_task.query.filter_by(task_id=task_id).first()
        if task:
            print task.middle_result_name
            package = openxl(task.middle_result_name)
        print "task_id:", task_id
       # cur.close()
       # conn.close()
        return render_template('show.html', package=package)
    return render_template('welcome.html', form=task_form)

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
        cur, conn = init_database('127.0.0.1', 'root', 'toor', 'mapper')
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
