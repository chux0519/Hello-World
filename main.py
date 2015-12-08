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
	__tablename__='patients'
	num=database.Column(database.Integer,primary_key=True)
	Name=database.Column(database.String(50))
	Sex =database.Column(database.String(50))
	Age =database.Column(database.String(50))
	Address=database.Column(database.String(200))
	Sympthon=database.Column(database.String(200))
	Analyze_=database.Column(database.String(200))

class LoginForm(Form):
	username = TextField("username",[validators.Required()])
	password = PasswordField("password",[validators.Required()])


class pa_Form(Form):
	name = TextField("name",[validators.Required()])
	sex = TextField("sex",[validators.Required()])
	age = TextField("age",[validators.Required()])
	address = TextField("address",[validators.Required()])
	sympthon = TextField("sympthon",[validators.Required()])

@app.route("/login",methods =['GET','POST'])
def login():
	loginform = LoginForm(request.form)
	msg=u"用户登陆"
	if request.method=='POST':
		name=loginform.username.data
		pwd=loginform.password.data
		if identify_Admin(name,pwd):
			msg= "Welcom,Administrator:%s!"%(name)
			return render_template('welcom.html',message=msg)
		if identify_User(name,pwd):
			msg="Welcom,%s"%name
			pa_result=session.query.filter_by(Name=name).order_by(session.num).all()
			len_pa=len(pa_result)
			print "####################################%s"%pa_result
			print"!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!%s"%len_pa
			#pa_result=session.query.filter_by(Name=name).first()
			#print "####################################%s"%pa_result
			ppaform=pa_Form(request.form)
			return render_template('pa_welcome.html',message=name,data=pa_result,paform=ppaform,len=len_pa)
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

@app.route('/scan/<Name>',methods=['GET','POST'])
def scan(Name):
	Name1=request.args.get("Name","")
	if Name1=="":
		pass
	result = session.query.filter_by(Name=Name).first()
	if result is None:
		json_result={'Name':None}
		return json.dumps(json_result,ensure_ascii=False)
	else:
		json_result={'num':result.num,'Name':result.Name,'Sex':result.Sex,'Age':result.Age,'Address':result.Address,'Sympthon':result.Sympthon,'Analyze_':result.Analyze_}
		return json.dumps(json_result,ensure_ascii=False)
@app.route("/index",methods =['GET','POST'])
def index():
	Name=request.args.get("Name","")
	if Name=="":
		msg="welcome"
		return render_template('admin.html',message=msg)
	else:
		print Name
		#return redirect(url_for('scan',Name=Name))
		return scan(Name)
	#msg="welcom"
	#return render_template('welcom.html',message=msg)

@app.route("/pa_register",methods=['GET','POST'])
def pa_reg():
	paform = pa_Form(request.form)
	if request.method=='POST':
		paname=paform.name.data
		sex=paform.sex.data
		age=paform.age.data
		addr=paform.address.data
		symp=paform.sympthon.data
		Pa_Reg(paname,sex,age,addr,symp)
		return "success!"
	else:
		return"fvck th GFW"


@app.route("/admin",methods =['GET','POST'])
def admin():
	Name=request.args.get("Name","")
	if Name=="":
		msg="welcome back,admin!"
		return render_template('admin.html',message=msg)
	else:
		#print Name
		result = session.query.filter_by(Name=Name).all()
		len_pa=len(result)
		if result is None:
			json_result={'Name':None}
			return json.dumps(json_result,ensure_ascii=False)
		else:
			prejson_result=[1,2]
			for i in range(0,len_pa):
				prejson_result[i]={'num':result[i].num,'Name':result[i].Name,'Sex':result[i].Sex,'Age':result[i].Age,'Address':result[i].Address,'Sympthon':result[i].Sympthon,'Analyze_':result[i].Analyze_}
			print prejson_result
			json_result={"patient":prejson_result}
			print json_result
			return json.dumps(json_result,ensure_ascii=False)	
if __name__=="__main__":
	app.run(port=8080)
