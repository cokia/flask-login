
from flask import *
from sqlalchemy import *
from sqlalchemy.orm import *
from flask_sqlalchemy import SQLAlchemy
import os
app = Flask(__name__)
#===============================================================================================
app.config['SECRET_KEY'] = 'https://github.com/cokia/flask-login' #You must edit this secret_key
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
di = "sqlite:///"+ os.path.join(os.getcwd(),"tmp","test.db")
app.config['SQLALCHEMY_DATABASE_URI'] = di
db = SQLAlchemy(app)
#===============================================================================================
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    db_userid = db.Column(String(15), unique=True)
    db_name = db.Column(String(50), unique=True)
    db_email = db.Column(String(120), unique=True)
    db_passwd = db.Column(String(15), unique=True) 
    def __repr__(self):
        return f"<User('{self.id}', '{self.db_name}', '{self.db_email}', '{self.db_userid}','{self.db_passwd}')>"
#===============================================================================================
db.init_app(app)
db.create_all()
#===============================================================================================
@app.route('/', methods=['GET', 'POST'])
def main():
	if session == False:
		return render_template('index.html')
	else:
		if request.method == 'POST':
			username = getname(request.form['username'])
			return render_template('index.html', data=getfollowedby(username))
		return render_template('index.html')
#===============================================================================================
@app.route('/admin', methods=['GET', 'POST'])
def admin():
	return "admin page"
#===============================================================================================
@app.route('/login', methods=['GET','POST'])
def login():
	if request.method == 'GET':
		return render_template('login.html')
	else: 
		userid = request.form['id']
		passwd = request.form['pass']
		
		try:
			data = User.query.filter_by(db_userid==userid, db_passwd==passwd).first()
			if data is not None:
				#db.session['login'] = True
				session = True
				return redirect(url_for('main'))
			elif data is not None & userid == admin:
				return redirect(url_for('admin'))
			else:
				return "I Can't Login, how about retry?"
		except:
			return "I Can't Login, how about retry?"
#===============================================================================================
@app.route('/register', methods=['GET','POST'])
def register():
	if request.method == 'GET':
		return render_template('register.html')
	elif request.method == 'POST':
		userid = request.form['id']
		passwd = request.form['pass']
		email = request.form['email']
		name = request.form['name']
		inputdata = User(db_userid = userid, db_name = name, db_email = email , db_passwd = passwd)
		db.session.add(inputdata)
		db.session.commit()
	else:
		return "nohack"
	return redirect(url_for('main'))
#===============================================================================================
@app.route('/logout', methods=['POST','GET']) 
def logout():
	session = False
	return redirect(url_for('main'))
#===============================================================================================
if __name__ == "__main__":
	app.run(host="0.0.0.0")