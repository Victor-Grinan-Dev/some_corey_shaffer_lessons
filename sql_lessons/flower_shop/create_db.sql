drop database if exists flowerdb;
create database flowerdb;

use flowerdb;

create table farmer(
    farmerId integer not null primary key,
    farmerName varchar(50) not null,
    farmLocation varchar(50),

)