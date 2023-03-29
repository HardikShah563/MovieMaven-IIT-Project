import psycopg2
import psycopg2.extras

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

create_script = ''' 
    create table if not exists users (
        u_id integer not null, 
        name varchar(100) not null,
        email varchar(100), 
        password varchar(200),
        isadmin boolean not null default false
    );
'''

cur.execute(create_script)
conn.commit()

create_script = ''' 
    create table if not exists venue (
        u_id integer not null, 
        name varchar(100) not null,
        email varchar(100), 
        password varchar(200),
        isadmin boolean not null default false
    );
'''

cur.execute(create_script)
conn.commit()

create_script = '''
    create sequence if not exists public.user_seq_no
        increment 1
        start 1
        minvalue 1
        maxvalue 99999
        owned by users.u_id;

    alter sequence public.user_seq_no
        owner to postgres;
'''

cur.execute(create_script)
conn.commit()

def registerAccount(name, email, password): 
    insert_script = '''
        select * from users where email = %s
    '''
    insert_values = ([email])
    cur.execute(insert_script, insert_values)
    conn.commit()
    if(cur.fetchall):
        return "Email Already exists! Log in if you have an account!"

    insert_script = '''
        insert into users (u_id, name, email, password) 
        values (NEXTVAL('user_seq_no'), %s, %s, %s)
    '''
    insert_values = (name, email, password)
    cur.execute(insert_script, insert_values)
    conn.commit()

    insert_script = '''
        select * from users where email = %s
    '''
    insert_values = ([email])
    cur.execute(insert_script, insert_values)
    conn.commit()

    return "New Account Registered!"

def loginAccount(email, password): 
    insert_script = '''
        select * from users where email = %s and password = %s
    '''
    insert_values = (email, password)
    cur.execute(insert_script, insert_values)
    if(cur): 
        msg = 'Login Successful!'
    else: 
        msg = 'Error loging in! Try again'
    conn.commit()

def getVenue(): 
    insert_script = '''
        select * from venue
    '''
    cur.execute(insert_script)
    conn.commit()

def getShows(): 
    insert_script = '''
        select 
    '''


# conn.close()
# cur.close()
# insert_script = '''
#         select * from users where email = %s
#     '''
# insert_values = (['hardikts@gmail.com'])
# cur.execute(insert_script, insert_values)
# # cur.execute(insert_script)
# data = cur.fetchall()
# conn.commit()
# print("Data: ", data)