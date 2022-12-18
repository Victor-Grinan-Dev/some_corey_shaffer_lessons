drop database if exists companydb4;
create database companydb4;

use companydb4;

create table department(
    departmentId integer not null primary key,
    departmentName varchar(20) not null,
    departmentFloor varchar(15) not null
);

create table employee(
    employeeId integer not null primary key,
    firstname varchar(20) not null,
    lastname varchar(30),
    salary decimal(6,2) not null
);

create table headOfDepartment(
    departmentId integer not null,
    employeeId integer not null,
    primary key(departmentId,employeeId),
    foreign key (departmentId) references department(departmentId),
    foreign key (employeeId) references employee(employeeId)
);

create table workerOfDepartment(
    departmentId integer not null,
    employeeId integer not null,
    primary key(departmentId,employeeId),
    foreign key (departmentId) references department(departmentId),
    foreign key (employeeId) references employee(employeeId)
);

insert into department values(1,'ict','basement');
insert into department values(2,'admin','top floor');
insert into department values(3,'secr','secret location');
insert into department values(4,'maintenance','workshop');
insert into department values(5, 'transportation', 'garage');

insert into employee values(1,'Mary','River',3000);
insert into employee values(2,'Matt','River',4000);
insert into employee values(3,'Amanda','Smith',7000);
insert into employee values(4,'Joe', 'Doe',9000);
insert into employee values(5,'Vera','Jones',6500 );
insert into employee values(6,'Peter','Bond', 3000);
insert into employee values(7,'Layla','Driver',5000);

insert into headOfDepartment values(1,3);
insert into headOfDepartment values(2,3);
insert into headOfDepartment values(3,4);
insert into headOfDepartment values(4,4);
insert into headOfDepartment values(5,3);

insert into workerOfDepartment values(1,1);

grant all privileges on companydb4.* to 'administrator'@'localhost';