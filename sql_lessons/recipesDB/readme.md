# Recipes database

to store recipes

recipes and ingredients needed

Country origin of the recipe
countries code3 (FIN, CUB, USA, etc) 
https://www.iban.com/country-codes
https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3

recipe:
-   id  (unique)
-   name
-   countrycode
-   instructions

ingredoients:
-   id  (unique)
-   name
-   picture

recipes_has_ingredient:
-   recipeNumber
-   ingredientNumber
-   amount
-   unit

task:

country should have name and 2 char code language
add images for recipe
country