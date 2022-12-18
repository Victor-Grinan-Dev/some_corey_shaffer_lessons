select * from ingredient;
select * from recipe;
select * from recipes_has_ingredient;

select user from mysql.user;

select * from recipe
inner join recipes_has_ingredient on recipeNumber=recipeId
inner join ingredient on ingredientNumber=ingredientId
where recipeName='cake';

select ingredientName, amount, unit from recipe
inner join recipes_has_ingredient on recipeNumber=recipeId
inner join ingredient on ingredientNumber=ingredientId
where recipeName='cake';

select ingredientName, amount, unit from recipe
inner join recipes_has_ingredient on recipeNumber=recipeId
inner join ingredient on ingredientNumber=ingredientId
where recipeName='pancake';

select recipeName from recipe 
inner join recipes_has_ingredient on recipeNumber=recipeId
inner join ingredient on ingredientNumber=ingredientId
where ingredientName='milk';

/*select all ingredients in use*/
select ingredientName, recipeName from ingredient 
left join recipes_has_ingredient on ingredientNumber=ingredientId
left join recipe on recipeNumber=recipeId;

/*select all ingredients NOT in use*/
select ingredientName from ingredient 
left join recipes_has_ingredient on ingredientNumber=ingredientId
where ingredientNumber is null;

/*select all ingredients in use. the name is only once*/
select distinct ingredientName from ingredient 
inner join recipes_has_ingredient on ingredientNumber=ingredientId;

/*get number of recipes by country*/
select countryCode, count(*) as numberOfRecepies from recipe 
group by countryCode
order by countryCode;

-- get the number of ingredients in each recipe NOT WORKING!!!
select recipeName, count(ingredientId) as 'number of ingredients' from recipe
inner join recipes_has_ingredient on recipeNumber=recipeId
inner join ingredient on ingredientNumber=ingredientId
group by recipeName;

update recipe set recipeName='pannukakku' where recipeId=3;

select recipeName, instructions from recipe;

--shopping list for cake and pancake (name ingredient name amount and units)

select ingredientName, amount, unit from recipe
inner join recipes_has_ingredient on recipeNumber=recipeId
inner join ingredient on ingredientNumber=ingredientId
where recipeName in ('cake','pancake')
order by ingredientName;


--list all images for cake
select imageName from recipeImage
inner join recipe on recipeRef=recipeId
where recipeName='cake';

