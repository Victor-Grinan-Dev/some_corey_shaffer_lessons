create database if not exists warhammer;

select user from mysql.user;


/*  FACTION */
create table if not exists faction(
    factionId integer primary key not null,
    factionName varchar(30) not null,
);

/* WEAPONS */

create table if not exists weapon(
    weaponId integer primary key not null,
    weaponName varchar(30) not null,
    weaponRange integer,
    weaponStregth integer not null,
);