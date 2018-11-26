from flask import *
from sqlalchemy import *
from db_init import base
app = Flask(__name__)

class User(base):
	__tablename__ = 'users'
	id = Column(String(15), primary_key=True)
	userid = Column(String(15), unique=True)
	name = Column(String(50), unique=True)
	email = Column(String(120), unique=True)
	passwd = Column(String(15), unique=True)

@app.route('/', methods=['GET', 'POST'])
def main():
	""" Session control"""
	if not session.get('login'):
		return render_template('index.html')
	else:
		if request.method == 'POST':
			username = getname(request.form['username'])
			return render_template('index.html', data=getfollowedby(username))
		return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
	if request.method == 'GET':
		return render_template('login.html')
	else: 
		userid = request.form['id']
		passwd = request.form['pass']
		try:
			data = User.query.filter_by(username=name, password=passw).first()
			if data is not None:
				session['login'] = True
				return redirect(url_for('main'))
			else:
				return "I Can't Login, how about retry?"
		except:
			return "I Can't Login, how about retry?"


@app.route('/register', methods=['POST'])
def register():
	return render_template('register.html')

@app.route('/logout', methods=['POST','GET']) 
def logout():
	session['login'] = False
	return redirect(url_for('main'))
	
	