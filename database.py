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
        isadmin boolean not null default false, 
        PRIMARY KEY (u_id)
        );

    create table if not exists venue (
        venue_id integer not null, 
        venue_name varchar(100) not null, 
        PRIMARY KEY (venue_id)
    );

    create table if not exists shows (
        show_id integer not null, 
        show_name varchar(100) not null, 
        show_time varchar(10) not null, 
        silver_cost integer not null, 
        gold_cost integer not null, 
        platinum_cost integer not null, 
        silver_count integer not null, 
        gold_count integer not null, 
        platinum_count integer not null, 
        silver_booked integer not null, 
        gold_booked integer not null, 
        platinum_booked integer not null, 
        venue_id integer not null, 
        venue_name varchar(100) not null, 
        PRIMARY KEY (show_id), 
        FOREIGN KEY (venue_id) REFERENCES venue (venue_id)
    );

    create table if not exists booking (
        booking_id integer not null, 
        u_id integer not null, 
        show_id integer not null, 
        silver_qty integer not null, 
        gold_qty integer not null, 
        platinum_qty integer not null, 
        total_cost integer not null, 
        PRIMARY KEY (booking_id), 
        FOREIGN KEY (show_id) REFERENCES shows(show_id),
        FOREIGN KEY (u_id) REFERENCES users(u_id)
    );
 
    create table if not exists rating (
        u_id integer not null,
        rate_id integer not null, 
        show_id integer not null, 
        rate_no integer not null, 
        rate_statement varchar(50), 
        PRIMARY KEY (rate_id), 
        FOREIGN KEY (show_id) REFERENCES shows (show_id),
        FOREIGN KEY (u_id) REFERENCES users (u_id)
    );

    create sequence if not exists public.user_seq_no
        increment 1
        start 1
        minvalue 1
        maxvalue 99999
        owned by users.u_id;

    alter sequence public.user_seq_no
        owner to postgres;

    create sequence if not exists public.venue_seq_no
        increment 1
        start 1
        minvalue 1
        maxvalue 99999
        owned by venue.venue_id;

    alter sequence public.venue_seq_no
        owner to postgres;

    create sequence if not exists public.booking_seq_no
        increment 1
        start 1
        minvalue 1
        maxvalue 99999
        owned by booking.booking_id;

    alter sequence public.booking_seq_no
        owner to postgres;

    create sequence if not exists public.rate_seq_no
        increment 1
        start 1
        minvalue 1
        maxvalue 99999
        owned by rating.rate_id;

    alter sequence public.rate_seq_no
        owner to postgres;

    create sequence if not exists public.show_seq_no
        increment 1
        start 1
        minvalue 1
        maxvalue 99999
        owned by shows.show_id; 

    alter sequence public.show_seq_no
        owner to postgres;
'''

cur.execute(create_script)
conn.commit()

def registerAccount(name, email, password): 
    insert_script = '''
        select u.email from users as u where email = %s
    '''
    insert_values = ([email])
    cur.execute(insert_script, insert_values)
    conn.commit()
    if(cur.fetchall()):
        return False

    insert_script = '''
        insert into users (u_id, name, email, password) 
        values (NEXTVAL('user_seq_no'), %s, %s, %s)
    '''
    insert_values = (name, email, password)
    cur.execute(insert_script, insert_values)
    if(conn.commit()): 
       return True

def loginAccount(email, password): 
    insert_script = '''
        select password from users where email = %s
    '''
    insert_values = ([email])
    cur.execute(insert_script, insert_values)
    conn.commit()
    data = cur.fetchall()
    if(data[0][0] == password): 
        return True
    else: 
        return False

def getUID(email): 
    insert_script = '''
        select u_id from users where email = %s
    '''
    insert_values = ([email])
    cur.execute(insert_script, insert_values)
    conn.commit()
    data = cur.fetchone()
    return data[0]

def getName(u_id): 
    insert_script = '''
        select name from users where u_id = %s
    '''
    insert_values = ([u_id])
    cur.execute(insert_script, insert_values)
    conn.commit()
    data = cur.fetchone()
    return data[0]

def isAdmin(u_id): 
    insert_script = '''
        select isAdmin from users where u_id = %s
    '''
    insert_values = ([u_id])
    cur.execute(insert_script, insert_values)
    conn.commit()
    data = cur.fetchone()
    return data[0]

def getVenue(): 
    get_script = '''
        select venue_name from venue
    '''
    cur.execute(get_script)
    conn.commit()
    data = cur.fetchall()
    venues = []
    for venue in data: 
        venues.append(venue[0])
    return venues


def getShows(): 
    get_script = '''
        select show_name from shows
    '''
    cur.execute(get_script)
    conn.commit()


    
    check_values = ([])

# conn.close()
# cur.close()

