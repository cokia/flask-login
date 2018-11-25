from flask import *
import sqlalchemy
app = Flask(__name__)

@app.route('/login')
def login():
    return render_template('login.html')

# @app.route('/login/<path:filename>')
# def login_file(filename):
#     return send_from_directory('login', filename)

@app.route('/register')
def register():
    return render_template('register.html')
app.run(host = "0.0.0.0")