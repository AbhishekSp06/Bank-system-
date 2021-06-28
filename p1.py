from flask import Flask,render_template,request
import cx_Oracle
app=Flask(__name__)
@app.route('/loginpage',methods=['GET','POST'])
def loginpage():
	return render_template("loginpage.html")
@app.route('/loginsuccess',methods=['GET','POST'])
def loginsuccess():
	return render_template("loginsuccess.html")
@app.route('/logincheck',methods=['GET','POST'])
def logincheck():
	sun=request.form['un']
	spw=request.form['pw']
	conn=cx_Oracle.connect('system','123456')
	curs=conn.cursor()
	query="select * from loginweb where username='%s' and password='%s'" %(sun,spw)
	curs.execute(query)
	rows=curs.fetchall()
	count=curs.rowcount
	if count==1:
		return render_template("loginsuccess.html")
	else:
		return render_template("loginfail.html")	
@app.route('/insertbackend',methods=['GET','POST'])
def insertbackend():
	sname=request.form['stuname']
	susn=request.form['stuusn']
	ssem=request.form['stusem']
	ssec=request.form['stusec']
	conn=cx_Oracle.connect('system','123456')
	curs=conn.cursor()
	query="insert into studentweb values('%s','%s',%d,'%s')" %(sname,susn,int(ssem),ssec)
	curs.execute(query)
	conn.commit()
	curs.close()
	conn.close()
	return render_template("insertsuccess.html")	
@app.route('/insertpage',methods=['GET','POST'])
def insertpage():
	return render_template("insertpage.html")
@app.route('/displayfrombackend',methods=['GET','POST'])
def displayfrombackend():
	conn=cx_Oracle.connect('system','123456')
	curs=conn.cursor()
	query="select * from studentweb"
	curs.execute(query)
	rows=curs.fetchall()
	return render_template("displaypage.html",hrows=rows)
@app.route('/deletepage',methods=['GET','POST'])
def deletepage():
	return render_template("deletepage.html")
@app.route('/deletefrombackend',methods=['GET','POST'])
def deletefrombackend():
	susn=request.form['stuusn']
	conn=cx_Oracle.connect('system','123456')
	curs=conn.cursor()
	query="delete from studentweb where usn='%s'" %(susn)
	curs.execute(query)
	conn.commit()
	curs.close()
	conn.close()
	return render_template("deletesuccess.html")
app.run(debug=True)