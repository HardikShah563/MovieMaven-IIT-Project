from flask import Flask, url_for, request, redirect, flash
from flask.templating import render_template
from werkzeug.security import generate_password_hash, check_password_hash
import psycopg2
import psycopg2.extras
from database import *
import hashlib

msg = ""


app = Flask(__name__)

# ---------------------------------------------

@app.route('/')
def index(): 
    return render_template('home.html')

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
        else: 
            className = "bg-red"
            msgText = "Login Un-Successful, try again!"

    return render_template('login.html', className = className,  msg = msgText)

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
        
    return render_template('register.html', className = className,  msg = msgText)

# ---------------------------------------------

@app.route('/bookShow', methods=["POST", "GET"])
def bookShow():

    return render_template('bookShow.html')

@app.route('/movies')
def movies():
    return render_template('movies.html')

@app.route('/u-dashboard')
def dashboard():
    return render_template('userDashboard.html')

@app.route('/ad-login')
def adminLogin():
    return render_template('admin-login.html')

@app.route('/ad-createshow')
def adminCreateShow():
    return render_template('admin-show-create.html')

@app.route('/ad-editshow')
def adminEditShow():
    return render_template('admin-show-edit.html')

@app.route('/ad-stats')
def adminStats():
    return render_template('admin-stats.html')

@app.route('/ad-createvenue')
def adminCreateVenue():
    return render_template('admin-venue-create.html')

@app.route('/ad-editvenue')
def adminEditVenue():
    return render_template('admin-venue-edit.html')

@app.route('/ad-view')
def adminView():
    return render_template('admin-view.html')

@app.route('/')
def logout():
    return render_template('home.html')






if __name__ == '__main__': 
    app.run(debug = True)