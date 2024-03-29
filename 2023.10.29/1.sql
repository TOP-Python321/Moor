--Запросы к таблице doctors:

--1. Вывести средний оклад (salary) всех сотрудников
--2. Вывести среднюю премию для всех сотрудников, чей доход выше среднего (взять явное значение из результата предыдущего запроса)

select
    avg(salary) as average_salary,
    avg(premium) as average_premium
from
    doctors
where
    salary > (select avg(salary) from doctors);
	
-- +----------------+-----------------+
-- | average_salary | average_premium |
-- +----------------+-----------------+
-- |   97017.647059 |    21681.382353 |
-- +----------------+-----------------+

 --Запросы к таблице vacations:

--3. Вывести с сортировкой по возрастанию среднее количество дней в отпуске для каждого сотрудника — используйте функцию datediff()

select doctors_id, 
	   round(avg(datediff(end_date, start_date))) as avg_days
from vacations
group by doctors_id
order by avg_days asc;

-- +------------+----------+
-- | doctors_id | avg_days |
-- +------------+----------+
-- |         37 |     1796 |
-- |          2 |     1884 |
-- |         47 |     2159 |
-- |         68 |     2160 |
-- |         63 |     2160 |
-- |         11 |     2191 |
-- |.......................|
-- +------------+----------+

--4. Вывести для каждого сотрудника самый ранний год отпуска и самый поздний год отпуска с сортировкой по возрастанию разности между этими двумя значениями

select doctors_id, 
	   min(year(start_date)) as earliest_year, 
	   max(year(start_date)) as latest_year, 
	  (max(year(start_date)) - min(year(start_date))) as year_difference
from vacations
group by doctors_id
order by year_difference asc;

-- +------------+---------------+-------------+-----------------+
-- | doctors_id | earliest_year | latest_year | year_difference |
-- +------------+---------------+-------------+-----------------+
-- |         34 |          2001 |        2007 |               6 |
-- |         57 |          2001 |        2010 |               9 |
-- |         27 |          2001 |        2013 |              12 |
-- |         70 |          2002 |        2014 |              12 |
-- |         49 |          2001 |        2013 |              12 |
-- |............................................................|
-- +------------+---------------+-------------+-----------------+
 
 -- Запросы к таблице donations:

-- 5. Вывести сумму пожертвований за всё время для каждого отделения с сортировкой по возрастанию номеров отделений

select departments_id, 
	   sum(amount) as all_donations 
from donations 
group by departments_id 
order by departments_id asc;

-- 6. Вывести сумму пожертвований за каждый год для каждого спонсора с сортировкой по возрастанию номеров спонсоров и годов

select sponsors_id,
	   year(date) as year,
       sum(amount) as donations_per_year
from donations
group by sponsors_id, year(date)
order by sponsors_id, year(date) asc;

-- +-------------+------+--------------------+
-- | sponsors_id | year | donations_per_year |
-- +-------------+------+--------------------+
-- |           1 | 2008 |         2031320.00 |
-- |           1 | 2022 |           26000.00 |
-- |           1 | 2023 |           10000.00 |
-- |           2 | 2004 |          245080.00 |
-- |           2 | 2005 |         1629290.00 |
-- |           2 | 2007 |         1580363.00 |
-- |           2 | 2009 |         2531422.00 |
-- |           2 | 2016 |         1843308.00 |
-- |           2 | 2018 |          947229.00 |
-- |           2 | 2022 |         1856049.00 |
-- |           3 | 2003 |          803356.00 |
-- |           3 | 2007 |          685092.00 |
-- |           3 | 2018 |          388077.00 |
-- |.........................................|
-- +-------------+------+--------------------+