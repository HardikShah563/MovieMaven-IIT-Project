from flask import Flask, url_for, request, redirect, flash, session
from flask.templating import render_template
from flask_session import Session
from werkzeug.security import generate_password_hash, check_password_hash
import psycopg2
import psycopg2.extras
from database import *
import hashlib

msg = ""
# session = []
# session.append(0)
# session.append("")
# session.append("")
# session.append(True)
# # session[0] = u_id
# # session[1] = name
# # session[2] = email
# # session[3] = isAdmin
# # Values inserted during login

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# ---------------------------------------------

@app.route('/')
def index(): 
    return render_template('home.html', session = session)

# ---------------------------------------------

@app.route('/login', methods=["POST", "GET"])
def login():
    className = ""
    msgText = ""
    if request.method == 'POST': 
        email = request.form['email']
        password = hash(request.form['password'])
        password = hashlib.sha256(request.form['password'].encode('utf-8')).hexdigest()
        password = password[0:9]
        msg = loginAccount(email, password)
        if(msg): 
            className = "bg-green"
            msgText = "Login Successful!" 
            
            session['u_id'] = getUID(email)
            session['name'] = getName(email)
            session['email'] = email
            session['isAdmin'] = adminCheck(email)
        else: 
            className = "bg-red"
            msgText = "Login Un-Successful, try again!"

    return render_template('login.html', className = className,  msg = msgText, session = session)

# ---------------------------------------------

@app.route('/register', methods=["POST", "GET"])
def register():
    msg = False
    className = ""
    msgText = ""
    if request.method == 'POST': 
        name = request.form['name']
        email = request.form['email']
        password = hashlib.sha256(request.form['password'].encode('utf-8')).hexdigest()
        password = password[0:9]
        msg = registerAccount(name, email, password)
        if(msg): 
            className = "bg-green"
            msgText = "New Account Registered!"
        else: 
            className = "bg-red"
            msgText = "Email Already exists! Log in if you have an account!"
        
    return render_template('register.html', className = className,  msg = msgText, session = session)

# ---------------------------------------------

@app.route('/bookShow', methods=["POST", "GET"])
def bookShow():
    # if request.method == 'POST': 

    return render_template('bookShow.html', session = session)

@app.route('/movies', methods=["POST", "GET"])
def movies():
    venues = getVenue()
    shows = getShows()
    return render_template('movies.html', session = session, venues = venues, len = len(venues), shows = shows)

@app.route('/u-dashboard', methods=["POST", "GET"])
def dashboard():
    return render_template('userDashboard.html', session = session)

@app.route('/ad-login', methods=["POST", "GET"])
def adminLogin():
    className = ""
    msgText = ""
    if request.method == 'POST': 
        email = request.form['email']
        password = hash(request.form['password'])
        password = hashlib.sha256(request.form['password'].encode('utf-8')).hexdigest()
        password = password[0:9]
        msg = loginAccount(email, password)
        if(msg): 
            className = "bg-green"
            msgText = "Login Successful!" 
            
            session['u_id'] = getUID(email)
            session['name'] = getName(email)
            session['email'] = email
            session['isAdmin'] = adminCheck(email)
            return redirect("/ad-view")
        else: 
            className = "bg-red"
            msgText = "Try again with admin credentials!!"
    return render_template('admin-login.html', className= className, msg = msgText, session = session)

@app.route('/ad-createshow', methods=["POST", "GET"])
def adminCreateShow(): 
    return render_template('admin-show-create.html', session = session)

@app.route('/ad-editshow', methods=["POST", "GET"])
def adminEditShow():
    return render_template('admin-show-edit.html', session = session)

@app.route('/ad-stats', methods=["POST", "GET"])
def adminStats():
    return render_template('admin-stats.html', session = session)

@app.route('/ad-createvenue', methods=["POST", "GET"])
def adminCreateVenue():
    return render_template('admin-venue-create.html', session = session)

@app.route('/ad-editvenue', methods=["POST", "GET"])
def adminEditVenue():
    
    return render_template('admin-venue-edit.html', session = session)

@app.route('/ad-view', methods=["POST", "GET"])
def adminView():
    return render_template('admin-view.html', session = session)

@app.route('/logout')
def logout():
    session["u_id"] = None
    session["name"] = None
    session["email"] = None
    session["isAdmin"] = None
    return redirect("/")



if __name__ == '__main__': 
    app.run(debug = True)