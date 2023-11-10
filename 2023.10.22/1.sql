-- Запросы к таблице country:

-- 1. Вывести названия всех стран Евразии

select name 
from country
where continent = 'Europe' or continent = 'Asia';

-- +-------------------------------+
-- | name                          |
-- +-------------------------------+
-- | Afghanistan                   |
-- | Albania                       |
-- | Andorra                       |
-- | United Arab Emirates          |
-- | Armenia                       |
-- | Austria                       |
-- |...............................|
-- +-------------------------------+
-- 97 rows in set (0.0011 sec)

-- 2. Вывести названия регионов и стран, в которых ожидаемая продолжительность жизни меньше пятидесяти лет

select region,
       name
from country 
where LifeExpectancy < 50;

-- +---------------------------+---------------------------------------+
-- | region                    | name                                  |
-- +---------------------------+---------------------------------------+
-- | Southern and Central Asia | Afghanistan                           |
-- | Central Africa            | Angola                                |
-- | Eastern Africa            | Burundi                               |
-- | Western Africa            | Burkina Faso                          |
-- | Southern Africa           | Botswana                              |
-- |...................................................................|
-- +---------------------------+---------------------------------------+
-- 28 rows in set (0.0010 sec)

-- 3. Вывести название самой крупной по площади страны Африки

select name
from country
where surfacearea = (
	select max(surfacearea)
	from country 
	where continent = 'Africa'
);

-- +-------+
-- | name  |
-- +-------+
-- | Sudan |
-- +-------+
-- 1 row in set (0.0012 sec)

-- 4. Вывести названия пяти азиатских стран с самой низкой плотностью населения

select name 
from country
where continent = 'Asia'
order by population / surfacearea
limit 5;

-- +--------------+
-- | name         |
-- +--------------+
-- | Mongolia     |
-- | Kazakstan    |
-- | Oman         |
-- | Turkmenistan |
-- | Saudi Arabia |
-- +--------------+
-- 5 rows in set (0.0015 sec)

-- Запросы к таблице city

-- 5. Вывести в порядке возрастания населения коды стран и названия городов, численность населения которых превышает пять миллионов человек

select countrycode, 
	   name
from city
where population > 5000000
order by population;

-- +-------------+-------------------+
-- | countrycode | name              |
-- +-------------+-------------------+
-- | PAK         | Lahore            |
-- | COD         | Kinshasa          |
-- | CHN         | Tianjin           |
-- | BRA         | Rio de Janeiro    |
-- | COL         | Santafé de Bogotá |
-- | THA         | Bangkok           |
-- | CHN         | Chongqing         |
-- | PER         | Lima              |
-- | IRN         | Teheran           |
-- | EGY         | Cairo             |
-- | IND         | Delhi             |
-- | GBR         | London            |
-- | CHN         | Peking            |
-- | JPN         | Tokyo             |
-- | USA         | New York          |
-- | RUS         | Moscow            |
-- | MEX         | Ciudad de México  |
-- | TUR         | Istanbul          |
-- | PAK         | Karachi           |
-- | IDN         | Jakarta           |
-- | CHN         | Shanghai          |
-- | BRA         | São Paulo         |
-- | KOR         | Seoul             |
-- | IND         | Mumbai (Bombay)   |
-- +-------------+-------------------+
-- 24 rows in set (0.0027 sec)

-- 6. Вывести название города в Индии с самым длинным названием

select name
from city
where countrycode = 'IND'
order by length(name) desc limit 1;

-- +--------------------------------+
-- | name                           |
-- +--------------------------------+
-- | Thiruvananthapuram (Trivandrum |
-- +--------------------------------+
-- 1 row in set (0.0015 sec)