drop table if exists recipesdb2;
create database recipesdb2;

use recipesdb2;

create table country(
    countrId varchar(3) not null primary key,
    countryName varchar(50) not null, 
    code2Name varchar(2),
    primaryLanguage varchar(20)
);

create table recipe( 
    recipeId integer not null primary key,
    recipeName varchar(100) not null,
    countryCode varchar(3),
    instructions varchar(1000),
    foreign key (countryCode) references country(countryId)
);

create table ingredient(
    ingredientId integer not null primary key,
    ingredientName varchar(40) not null, 
    pictureName varchar(30)
);

create table recipes_has_ingredient(
    recipeNumber integer not null,
    ingredientNumber integer not null, 
    amount decimal(5,2) not null, 
    unit varchar(10) not null,
    primary key (recipeNumber, ingredientNumber),
    foreign key (recipeNumber) references recipe(recipeId),
    foreign key (ingredientNumber) references ingredient(ingredientId)
);


create table images(
    imgId integer not null primary key,
    imgName varchar(50) not null, 
    altText varchar(20),
    imgFilename varchar(100)
);
  
drop user if exists 'baker'@'localhost';
create user 'baker'@'localhost' indentified by 'cake123';
grant all privileges on recipesdb.* to 'baker'@'localhost';


insert into country values('FIN', 'Finland', 'FI', 'Finnish');
insert into country values('SWE', 'Sweeden', 'SW', 'Sweedish');


insert into recipe values(1, 'cake', 'FIN', 'bake a cake...');
insert into recipe values(2, 'pancake', 'SWE', 'panfry a pancake...');
insert into recipe values(3, 'pancake', 'FIN', 'panfry a pancake...');

insert into ingredient values(1, 'flour', 'flour.png');
insert into ingredient values(2, 'sugar', 'sugar.png');
insert into ingredient values(3, 'egg', 'egg.png');
insert into ingredient values(4, 'baking powder', 'baking_powder.png');
insert into ingredient values(5, 'milk', 'milk.png');
insert into ingredient values(6, 'oil', null);
insert into ingredient values(7, 'butter', 'butter.png');
insert into ingredient values(8, 'salt', 'salt.png');

insert into recipes_has_ingredient values(1,1,3.5,'dl');
insert into recipes_has_ingredient values(1,2,1,'handfull');
insert into recipes_has_ingredient values(1,3,3,'big ones');
insert into recipes_has_ingredient values(2,7,150,'g');
insert into recipes_has_ingredient values(2,1,0.5,'l');
insert into recipes_has_ingredient values(2,3,1,'cup');
insert into recipes_has_ingredient values(2,4,0.5,'spoon');
insert into recipes_has_ingredient values(2,5,1,'l');
insert into recipes_has_ingredient values(2,6,1,'dl');

alter table images
add recipeRef integer not null;

create table recipe_has_image(
    recipeRef integer not null,
    imageRef integer not null,
    primary key(recipeRef, imageRef),
    foreign key recipe_has_image(recipeRef) references recipe(recipeId),
    foreign key recipe_has_image(imageRef) references images(imageId)
);