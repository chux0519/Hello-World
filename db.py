#coding:utf-8
import MySQLdb
conn =MySQLdb.connect("localhost","root","","his",read_default_file='/opt/lampp/etc/my.cnf')

cur=conn.cursor()

def addUser_User(username,password):
	sql ="insert into users(Name,Pwd) values('%s','%s')"%(username,password)
	cur.execute(sql)
	conn.commit()
	conn.close()
def identify_Admin(username,password):
	sql ="select * from admin where username='%s' and password = '%s'"%(username,password)
	cur.execute(sql)
	result = cur.fetchall()
	if(len(result)==0):
		return False
	else:
		return True
def identify_User(username,password):
	sql ="select * from users where Name='%s' and Pwd = '%s'"%(username,password)
	cur.execute(sql)
	result = cur.fetchall()
	if(len(result)==0):
		return False
	else:
		return True
def User_status(username,password):
	sql="select Status from users where Name='%s' and Pwd='%s'"%(username,password)
	cur.execute(sql)
	status = cur.fetchone()
	if(status=='1'):
		msg=u"您当前有可查看的诊断记录！"
		return msg
	else:
		msg=u"您当前暂无可查看的诊断记录！"
		return msg
def Patient_rec(name):
	sql="select Name,Sympthon  from patient where Name='%s'"%(name)
	cur.execute(sql)
	rec=(cur.fetchall())
	print rec[0]
	for each in rec:
		print each
	li=rec.__str__()
	print li
	conn.close()
def Pa_Reg(name,sex,age,addr,symp):
	sql="insert into patients (Name,Sex,Age,Address,Sympthon) values('%s','%s','%s','%s','%s')"%(name,sex,age,addr,symp)
	cur.execute(sql)
	conn.commit()
	conn.close()