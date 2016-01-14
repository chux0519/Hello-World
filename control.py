# encoding:utf-8
from flask import Flask, render_template, redirect, request
from openxl import *
app = Flask(__name__)
app.debug = True


@app.route('/')
def index():
    package = openxl("./59146.xls")
    return render_template('index.html', package=package)


@app.route('/map', methods=['POST', 'GET'])
def map():
    # master_arr = request.values.get('master_id', 0)
    status = "failed!"
    if request.method == 'POST':
        # master_arr = request.form.get(master_id, 0)
        data = request.get_json()
        print data
        status = "success!"
    return status

if __name__ == '__main__':
    app.run(port=8080)
