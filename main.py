#coding:utf-8
from flask import Flask,jsonify,json
from flask import request,url_for
from flask import render_template
from flask import redirect
from db import *
from flask.ext.sqlalchemy import SQLAlchemy

app =Flask(__name__)
app.debug=True
database=SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:%s@127.0.0.1/his'%('')

from wtforms import Form , TextField, PasswordField, validators

class session(database.Model):
	__tablename__='patient'
	num=database.Column(database.String(18),primary_key=True)
	Name=database.Column(database.String(50))
	Sex =database.Column(database.String(50))
	Age =database.Column(database.String(50))
	Address=database.Column(database.String(200))
	Sympthon=database.Column(database.String(200))
	Analyze_=database.Column(database.String(200))

class LoginForm(Form):
	username = TextField("username",[validators.Required()])
	password = PasswordField("password",[validators.Required()])
@app.route("/login",methods =['GET','POST'])
def login():
	loginform = LoginForm(request.form)
	msg=u"用户登陆"
	if request.method=='POST':
		name=loginform.username.data
		pwd=loginform.password.data
		if identify_Admin(name,pwd):
			return "Welcom,Administrator:%s!"%(name)
		if identify_User(name,pwd):
			status_msg=User_status(name,pwd)
			return u"%s您好，%s"%(name,status_msg)

		else:
			msg =u"登陆失败，请检查账号密码!"
			return render_template('index.html',message=msg,form=loginform)
	return render_template('index.html',message=msg,form = loginform)

@app.route("/register",methods =['GET','POST'])
def register():
	registerform = LoginForm(request.form)
	if request.method=='POST':
		addUser_User(registerform.username.data,registerform.password.data) 
		return"注册成功!"
	return render_template('register.html',form= registerform)

@app.route('/scan/<num>',methods=['GET'])
def scan(num):
	result = session.query.filter_by(num=num).first()
	if result is None:
		json_result={'num':None}
		return json.dumps(json_result,ensure_ascii=False)
	else:
		json_result={'num':result.num,'Name':result.Name,'Sex':result.Sex,'Age':result.Age,'Address':result.Address,'Sympthon':result.Sympthon,'Analyze_':result.Analyze_}
		return json.dumps(json_result,ensure_ascii=False)
if __name__=="__main__":
	app.run(port=8080)
