drop database if exists companydb2;
create database companydb2;

use companydb2;

create table department(
    departmentId integer not null primary key,
    departmentName varchar(20) not null,
    departmentFloor varchar(15) not null
);

create table employee(
    employeeId integer not null primary key,
    firstname varchar(20) not null,
    lastname varchar(30),
    salary decimal(6,2) not null,
    departmentNumber integer not null,
    foreign key (departmentNumber) references department(departmentId)
);

grant all privileges on companydb2.* to 'administrator'@'localhost';


insert into employee values(1,'Mary','River',3000,1);
insert into employee values(2,'Matt','River',4000,1);
insert into employee values(3,'Amanda','Smith',7000,2);
insert into employee values(4,'Joe', 'Doe',9000,3);
insert into employee values(5,'Vera','Jones',6500,2 );
insert into employee values(6,'Peter','Bond', 3000,5);
insert into employee values(7,'Layla','Driver',5000,5);