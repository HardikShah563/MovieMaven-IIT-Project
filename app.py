from flask import Flask, url_for, request, redirect, flash
from flask.templating import render_template
from werkzeug.security import generate_password_hash, check_password_hash
import psycopg2
import psycopg2.extras
import database

hostname = 'localhost'
database = 'moviemaven'
username = 'postgres'
pwd = 'Hardikts@563'
port_id = 5432

conn = None
cur = None

conn = psycopg2.connect(
    host = hostname,
    dbname = database,
    user = username,
    password = pwd,
    port = port_id
)

cur = conn.cursor(cursor_factory = psycopg2.extras.DictCursor)



app = Flask(__name__)

@app.route('/')
def index(): 
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register', methods=["POST", "GET"])
def register():
    if request.method == 'POST': 
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        hashed_password = hash(password)
        insert_script = '''
            insert into users (u_id, name, email, password) 
            values (NEXTVAL('user_seq_no'), %s, %s, %s)
        '''
        insert_values = (name, email, hashed_password)
        cur.execute(insert_script, insert_values)
        conn.commit()

    return render_template('register.html')

@app.route('/bookShow')
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