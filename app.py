from flask import *
from sqlalchemy import *
from flask import *
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base

app = Flask(__name__)
#===============================================================================================
engine = create_engine('sqlite:////tmp/test.db', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()
#===============================================================================================
def init_db():
    Base.metadata.create_all(bind=engine)

class db(Base):
	init_db()
	__tablename__ = 'users'
	id = Column(String(15), primary_key=True)
	userid = Column(String(15), unique=True)
	name = Column(String(50), unique=True)
	email = Column(String(120), unique=True)
	passwd = Column(String(15), unique=True)

@app.route('/', methods=['GET', 'POST'])
def main():
	if not db_session.get('login'):
		return render_template('index.html')
	else:
		if request.method == 'POST':
			username = getname(request.form['username'])
			return render_template('index.html', data=getfollowedby(username))
		return render_template('index.html')

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
			else:
				return "I Can't Login, how about retry?"
		except:
			return "I Can't Login, how about retry?"


@app.route('/register', methods=['POST'])
def register():
	return render_template('register.html')

@app.route('/logout', methods=['POST','GET']) 
def logout():
	db_session['login'] = False
	return redirect(url_for('main'))
	
if __name__ == "__main__":
	app.run(host="0.0.0.0")