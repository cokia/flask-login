from flask import *
from sqlalchemy import *
from flask import *
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from flask_sqlalchemy import SQLAlchemy
from modules.db import db

app = Flask(__name__)
#===============================================================================================
#===============================================================================================
@app.route('/', methods=['GET', 'POST'])
def main():
	if not db_session.get('login'):
		return render_template('index.html')
	else:
		if request.method == 'POST':
			username = getname(request.form['username'])
			return render_template('index.html', data=getfollowedby(username))
		return render_template('index.html')

@app.route('/admin', methods=['GET', 'POST'])

@app.route('/login', methods=['GET','POST'])
def login():
	if request.method == 'GET':
		return render_template('login.html')
	else: 
		userid = request.form['id']
		passwd = request.form['pass']
		
		try:
			data = User.query.filter_by(username=name, password=passw).first()
			if data is not None:
				db_session['login'] = True
				return redirect(url_for('main'))
			elif data is not None & userid == admin:
				return redirect(url_for('admin'))
			else:
				return "I Can't Login, how about retry?"
		except:
			return "I Can't Login, how about retry?"


@app.route('/register', methods=['GET','POST'])
def register():
	if request.method == 'GET':
		return render_template('register.html')
	elif request.method == 'POST':
		userid = request.form['id']
		passwd = request.form['pass']
		email = request.form['email']
		name = request.form['name']
		inputdata = User(name = name, userid = userid, email = email , passwd = passwd)
		db.session.add(inputdata)
		db.session.commit()
	else:
		return "nohack"

@app.route('/logout', methods=['POST','GET']) 
def logout():
	db_session['login'] = False
	return redirect(url_for('main'))
#=============================================================================================== ``	
if __name__ == "__main__":
	app.run(host="0.0.0.0")