import psycopg2
import psycopg2.extras

hostname = 'localhost'
database = 'moviemaven'
username = 'postgres'
pwd = 'Hardikts@563'
port_id = 5432

conn = None
cur = None

try:
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



    
except Exception as error: 
    print(error)

finally: 
    if conn is not None: 
        conn.close()
    if cur is not None: 
        cur.close()
