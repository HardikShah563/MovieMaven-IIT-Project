from flask import Flask, url_for
from flask.templating import render_template
# from flask_sqlalchemy import SQLAlchemy
import os
import psycopg2

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost/moviemaven'

# ########################################
# Making Database Connections
# ########################################
def get_db_connection():
    conn = psycopg2.connect(
        host = 'localhost',
        database = 'moviemaven',
        user = os.environ['DB_USERNAME'],
        passwrod = os.environ['DB_PASSWORD']
    )
    return conn

# ########################################
# Creating Routes
# ########################################
@app.route('/')
def index(): 
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('select * from users;')
    users = cur.fetchall()
    cur.close()
    conn.close()
    
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/register')
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