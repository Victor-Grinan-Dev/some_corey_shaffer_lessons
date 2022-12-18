/*Victor Grinan*/
/*Tasks
Create a folder for the project
Write create statements for the database
Create the database
Write Sql statements
Submit the project*/


/*1 Create a folder for the project*/


/*Create a folder for the project. Name the folder with Grinan_Victor_dog_project.*/

/*2 Write create statements for the database
Write create statements to create a database called dogdb.*/

create database dogdb;
use dogdb;
/*
Create a table dog, for dog data. Table columns are:
number integer
name varchar(43)
length integer
weightKg integer
breed varchar(27)
All columns are mandatory. The primary key is number.
*/

create table dog(
    number integer not null primary key,
    name varchar(43) not null,
    length integer not null,
    weightKg integer not null,
    breed varchar(27) not null
);

/*Add two insert statements into the create statements for testing.*/

insert into dog values(8, "fido", 20, 12, "sato");
insert into dog values(9, "chuchi", 30, 15, "chihuahua");
insert into dog values(10, "firulais", 30, 20, "dalmatian");
select * from dog;

/*Create user hugo@localhost with password D33l6IKj. Grant all necessary privileges to the user.*/

create user 'hugo'@'localhost' identified by 'D33l6IKj';
grant all privileges on dogdb to 'hugo'@'localhost';

/**Save all necessary create statements into a sql file 
Grinan_Victor_dog_createStatements.sql*/

/*
3 Create the database
Create the database with the create statements .
4 Write Sql statements
After each operation check the content of the database by selecting all data from the table.
Write sql statements, with which you can insert, update, delete and select the dog data.
*/

update dog set name="pachi" where name="chuchi";
select * from dog;

delete from dog where name="pachi";
select * from dog;

delete from dog where name="fido";
select * from dog;


/*Save sql statements into project folder as a sql file named Grinan_Victor_dog_sqlStatements.sql.*/

/***********************************************************************/


/*Insert data to the database
Insert following data to the dog database*/
/*number	name	length	weightKg	breed
4	Spot	30	5	muddypaw
7	Grand Duke of S.Q.L	70	20	datahound
5	Gigant Howler	40	25	watchdog
6	Hound of Basker W.I.11e	42	10	spaniel
1	Canine The III	35	15	lapdog
3	Rex	50	45	furry tail-wagger
2	Barky	20	13	bulldog*/
/*number	name	length	weightKg	breed*/
insert into dog values (4, 'Spot', 30, 5, 'muddypaw');
insert into dog values (7, 'Grand Duke of S.Q.L', 70, 20, 'datahound');
insert into dog values (5, 'Gigant Howler',	40,	25,	'watchdog');
insert into dog values (6, 'Hound of Basker W.I.11e', 42, 10, 'spaniel');
insert into dog values (1, 'Canine The III', 35, 15, 'lapdog');
insert into dog values (3, 'Rex',	50,	45,	'furry tail-wagger');
insert into dog values (2, 'Barky',	20,	13,	'bulldog');



/*Getting data
Select all columns
Create select statement with which you get all data of the dogs. All columns should be included in the resultset.*/
select * from dog;


/*Write a select statement, with which you get all data of the dogs. Include into the resultset only the columns number, name, length.*/
select  number, name, length from dog;

/*Select with on*/
/*Select all dogs, where the breed is bulldog*/
select  * from dog where breed='bulldog';
/*Select all dogs, where the name is Gigant Howler*/
select  * from dog where name='Gigant Howler';
/*Select all dogs, where the name is Hound of Basker W.I.11e*/
select  * from dog where name='Hound of Basker W.I.11e';


/*Update data
To see the efect of the operations, you might have to add some new data to the table before executing the operation.*/
/*Update dog (number is 6). New data is: name is Canine The III and length is 42*/
update dog set name="Canine The III", length=42 where number=6;

/*Update dog (number is 1). New data is: weightKg is 7 and length is 30*/
update dog set length=30, weightKg=7 where number=1;

/*Update dog (number on 7). New data is: length is 42 and name is Gigant Howler and weightKg is 25*/
update dog set length=42, name="Gigant Howler", weightKg=25 where number=7;

/*Update dog (number on 4). New data is: breed is furry tail-wagger and length is 42 and name is Spot*/
update dog set breed='furry tail-wagger', name="Spot", length=42 where number=4;

/*Delete data
To see the efect of the operations, you might have to add some new data to the table before executing the operation.*/

insert into dog values(8, "fido", 20, 12, "sato");
insert into dog values(9, "chuchi", 30, 15, "chihuahua");
insert into dog values(10, "firulais", 30, 20, "dalmatian");

/*Delete dog, where number is 4*/
delete from dog where number=4;

/*Delete dog, where number is 6*/
delete from dog where number=6;

/*Delete all dogs, where breed is spaniel*/
delete from dog where breed="spaniel";

/*Delete all dogs, where length is 20 or weightKg is 15*/
delete from dog where length=20 or weightKg=15;

/*Delete all dogs, where weightKg is 45 or breed is furry tail-wagger or weightKg is 20*/
delete from dog where weightKg=45 or breed='furry tail-wagger' or weightKg=20;

/*5 Submit the project
Submit your project folder Grinan_Victor_dog_project acording to instructions given separately.*/