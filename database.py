import psycopg2

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

    cur = conn.cursor()

    create_script = ''' 
        create table if not exists users (
            u_id integer not null, 
            name varchar(50) not null,
            email varchar(50), 
            password varchar(50),
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

    insert_script = ''' 
        insert into users (u_id, name, email, password) 
        values (NEXTVAL('user_seq_no'), %s, %s, %s)
    '''
    insert_values = ('Hardik Shah', 'hardikts@gmail.com', 'hardikshah')
    cur.execute(insert_script, insert_values)
    conn.commit()



    
except Exception as error: 
    print(error)
finally: 
    if conn is not None: 
        conn.close()
    if cur is not None: 
        cur.close()

