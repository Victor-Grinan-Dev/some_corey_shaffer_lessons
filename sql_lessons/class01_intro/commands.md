

header1 | header2 | header3
:--- | ---: | :---:
data1 | data | data


| Description                                       | Command                                       |
| :--------------------------------                 | :--------------------                         |
| To login (from unix shell) use -h only if needed. | [mysql dir]/bin/mysql -h hostname -u root -p  |
| Create a database on the sql server.| create database [databasename];|
| List all databases on the sql server.| show databases;|
| Switch to a database.| use [db name];|
| To see all the tables in the db.| show tables;|
| To see database's field formats.| describe [table name];|
| To delete a db.	drop database|  [database name];|
| To delete a table.| drop table [table name];|
| Show all data in a table.| SELECT * FROM [table name];|
| Returns the columns and column information pertaining to the designated table.| show columns from [table name];|
| Show certain selected rows with the value "whatever". SELECT * FROM [table name] WHERE [field name] = "whatever";|
| Show all records containing the name "Bob" AND the phone number '3444444'.| SELECT * FROM [table name] WHERE name = "Bob" AND phone_number = '3444444';|
|Show all records not containing the name "Bob" AND the phone number '3444444' order by the phone_number field.| SELECT * FROM [table name] WHERE name != "Bob" AND phone_number = '3444444' order by phone_number;|
| Show all records starting with the letters 'bob' AND the phone number '3444444'.| SELECT * FROM [table name] WHERE name like "Bob%" AND phone_number = '3444444';|
| Use a regular expression to find records. Use "REGEXP BINARY" to force case-sensitivity. This finds any record beginning with a.| SELECT * FROM [table name] WHERE rec RLIKE "^a$";|
| Show unique records.| SELECT DISTINCT [column name] FROM [table name];|
| Show selected records sorted in an ascending (asc) or descending (desc).| SELECT [col1],[col2] FROM [table name] ORDER BY [col2] DESC;|
|Count rows.|SELECT COUNT(*) FROM [table name];|
|Join tables on common columns.| select lookup.illustrationid, lookup.personid,person.birthday from lookup|
| :--------------------------------                 | :--------------------                         |
| :--------------------------------                 | :--------------------                         |



	
	
	
	
	
	

	
	
		
	
		
		
	
		
	
	
		
	
left join person on lookup.personid=person.personid=statement to join birthday in person table with primary illustration id;
Switch to the mysql db. Create a new user.	