create table users (
    u_id integer AUTOINCREMENT PRIMARY key, 
    fullname text not null, 
    email text not null, 
    password text not null, 
    admin boolean not null DEFAULT '0'
);

create table venue (
    venue_id integer AUTOINCREMENT PRIMARY key, 
    venue_name text not null, 
);

create table show (
    show_id integer AUTOINCREMENT PRIMARY key, 
    show_name text not null, 
    venue_name text not null, 
    silver integer not null, 
    gold integer not null, 
    platinum integer not null, 
    silver_booked integer not null DEFAULT 0, 
    gold_booked integer not null DEFAULT 0, 
    platinum_booked integer not null DEFAULT 0, 
);

create table rating (
    show_id integer not null, 
    rating integer not null
);