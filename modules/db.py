from flask import *
from sqlalchemy import *
from flask import *
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#===============================================================================================
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)
#===============================================================================================
class User(db.Model):
	__tablename__ = 'user'
	id = db.Column(db.Integer, primary_key=True)
	userid = Column(String(15), unique=True)
	name = Column(String(50), unique=True)
	email = Column(String(120), unique=True)
	passwd = Column(String(15), unique=True)