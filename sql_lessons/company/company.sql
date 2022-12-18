create database if not exists companydb;

use companydb;

select user from mysql.user;
drop user if exists 'admin'@'localhost';
create user 'admin'@'localhost' identified by '1234';
grant all privileges on companydb to 'admin'@'localhost';


create table department(
    departmentId integer not null primary key,
    departmentName varchar(20) not null,
    departmentFloor varchar(15) not null
);

create table employee(
    employeeId integer not null primary key,
    firstname varchar(20) not null,
    lastname varchar(20) not null,
    salary decimal(6,2) not null,
    departmentNumber integer not null, 
    foreign key (departmentNumber) references department(departmentId)
);

insert into department values(1, 'ict', 'basement');
insert int department values(2, 'admin', 'top floor');
insert into department values(3, 'secr', 'secret location');
insert into department values(4, 'maintenance', 'workshop');
insert into department values(5, 'transportation', 'garage');

insert into employee values(1, 'Mary', 'River', 3000, 1);
insert into employee values(2, 'Matt', 'River', 4000, 1);
insert into employee values(3, 'Amanda', 'Smith', 7000, 2);
insert into employee values(4, 'Joe', 'Doe', 9000, 3);
insert into employee values(5, 'Vera', 'Jones', 6500, 2);
insert into employee values(6, 'Peter', 'Bond', 3000, 5);
insert into employee values(7, 'Layla', 'Driver', 5000, 5); 


select departmentName from employee, department where departmentNumber=departmentId and firstname='Mary';

/*old way to join tables*/
select firstname,lastname,departmentName from employee,department where departmentNumber=departmentId and departmentName='ict';

/* New way */
select firstname, lastname, departmentName from employee 
 inner join department on departmentNumber=departmentId
 where departmentName='ict';

select firstname, lastname, departmentName from employee 
 inner join department on departmentNumber=departmentId;

/**/
select firstname, lastname, departmentName from employee 
 inner join department on departmentNumber=departmentId
 order by lastname asc;

/* find Amandas name, department name, department floor and salary */
select firstname, departmentName, departmentFloor, salary 
from employee inner join department 
on departmentNumber=departmentId 
where firstname="Amanda";

/*calculate the average of the salary in ict department*/
select avg(salary) as average_salary, departmentName from employee inner join department where departmentName="ict";

select firstname, lastname, departmentName, salary, case 
when salary>(select avg(salary) from employee) then 'above average'
when salary<(select avg(salary) from employee) then 'below average'
else 'average' end as 'salary level'
from employee inner join department on departmentNumber=departmentId;

select firstname, lastname, departmentName, salary, case 
when salary>(select avg(salary) from employee) then 'above avg' when salary<(select avg(salary) from employee) then 'below avg' else 'average' end as 'salary level' from employee inner join department on departmentNumber=departmentId;

update department set departmentName='computerDept' where departmentId=1;

update department set departmentName='transp.' where departmentName="transportation";

/**/