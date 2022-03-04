from flask import Flask, render_template,request,redirect,url_for
import os

from flask_sqlalchemy import SQLAlchemy

app = None
db = SQLAlchemy()


def create_app():
    current_dir = os.path.abspath(os.path.dirname(__file__))
    app = Flask(__name__, template_folder='templates')
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + os.path.join(current_dir, 'database.sqlite3')
    db.init_app(app)
    app.app_context().push()
    return app


app = create_app()


@app.route("/")
def home():
  return render_template('login.html')

@app.route("/create")
def create():
  
  return render_template('Add_Tracker.html')

@app.route("/login", methods=["POST"])
def login():
  username=request.form.get("username")
  password=request.form.get("password")
  m1="Invalid Password! Try Again"
  m2="Username Does not exist! Try Again"
  
  
  #assume the desired password to be "pwd" and username to be "Name1"
  
  
  
  if username=="Name1" and password=="pwd":
  
    return render_template('welcome.html',name=username)
  elif username=="Shreyansh" and password!="abc":
    return render_template("login.html",message=m1)
  else:
    return render_template("login.html",message=m2)
    
    



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
