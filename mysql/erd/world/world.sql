SELECT * FROM countries; -- countries.code
SELECT * FROM cities; -- citis.country_id
SELECT * FROM languages; -- languages.country_id

-- 1. What query would you run to get all the countries that speak Slovene? 
-- Your query should return the name of the country, language and language 
-- percentage. Your query should arrange the result by language percentage 
-- in descending order. (1)
SELECT name, language, percentage FROM countries
JOIN languages ON countries.id = languages.country_id
WHERE languages.language LIKE 'Slovene'
ORDER BY percentage DESC;

-- 2. What query would you run to display the total number of cities for each 
-- country? Your query should return the name of the country and the total number
--  of cities. Your query should arrange the result by the number of cities in 
--  descending order. (3)
SELECT countries.name, COUNT(cities.name) AS cities FROM countries
JOIN cities ON countries.id = cities.country_id
GROUP BY countries.name
ORDER BY cities DESC;


-- 3. What query would you run to get all the cities in Mexico with a population
--  of greater than 500,000? Your query should arrange the result by population 
--  in descending order. (1)

SELECT cities.name, cities.population, country_id FROM cities
JOIN countries ON cities.country_id = countries.id
WHERE cities.population > 500000 AND countries.name LIKE 'Mexico';


-- 4. What query would you run to get all languages in each country with a percentage 
-- greater than 89%? Your query should arrange the result by percentage in descending
--  order. (1)

SELECT countries.name, language, percentage FROM languages
JOIN countries ON languages.country_id = countries.id
WHERE percentage > 98
ORDER BY percentage DESC;


-- 5. What query would you run to get all the countries with Surface Area below 501 
-- and Population greater than 100,000? (2)

SELECT name, surface_area, population FROM countries
WHERE surface_area < 501 AND population > 100000;

-- 6. What query would you run to get countries with only Constitutional Monarchy 
-- with a capital greater than 200 and a life expectancy greater than 75 years? (1)

SELECT name, government_form, capital, life_expectancy FROM countries
WHERE capital > 200 AND life_expectancy > 75;

-- 7. What query would you run to get all the cities of Argentina inside the Buenos
--  Aires district and have the population greater than 500, 000? The query should 
--  return the Country Name, City Name, District and Population. (2)

SELECT countries.name AS country_name, cities.name AS city_name, district, cities.population FROM cities
JOIN countries ON cities.country_id = countries.id
WHERE cities.population > 500000 AND countries.name LIKE 'Argentina' AND district LIKE 'Buenos Aires';

-- 8. What query would you run to summarize the number of countries in each region? 
-- The query should display the name of the region and the number of countries. Also,
--  the query should arrange the result by the number of countries in descending order. (2)

SELECT region, COUNT(countries.name) FROM countries
GROUP BY region;