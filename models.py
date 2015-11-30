#models.py
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root@127.0.0.1/his'
db=SQLAlchemy(app)
class patients(db.Model):
	#__tablename__='patient'
	num=db.Column(db.Integer,primary_key=True)
	Name=db.Column(db.String(50))
	Sex =db.Column(db.String(50))
	Age =db.Column(db.String(50))
	Address=db.Column(db.String(200))
	Sympthon=db.Column(db.String(200))
	Analyze_=db.Column(db.String(200))
	def __init__(self,Name,Sex,Age,Address,Sympthon,Analyze_):
		self.Name=Name
		self.Sex=Sex
		self.Age=Age
		self.Address=Address
		self.Sympthon=Sympthon
		self.Analyze_=Analyze_
	def add(self):
		try:
			db.session.add(self)
		 	db.session.commit()
		 	return self.num
		except Exception,e:
		 	db.session.rollback()
		 	return e
		finally:
		 	return 0