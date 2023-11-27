-- Запросы к таблицам схемы world

-- 1. Вывести названия стран и названия сопоставленных им столиц


select country.name, city.name 
	from country join city 
		on country.capital = city.id;
	
-- +---------------------------------------+-----------------------------------+
-- | name                                  | name                              |
-- +---------------------------------------+-----------------------------------+
-- | Aruba                                 | Oranjestad                        |
-- | Afghanistan                           | Kabul                             |
-- | Angola                                | Luanda                            |
-- | Anguilla                              | The Valley                        |
-- | Albania                               | Tirana                            |
-- | Andorra                               | Andorra la Vella                  |
-- +---------------------------------------+-----------------------------------+
-- 232 rows in set (0.0022 sec)


-- 2. Сравнить по регионам сумму населения стран и сумму населения городов

select region, sum(country.population) - sum(city.population) as `difference`
	from country 
	join city
    on country.code = city.countrycode
group by region;

-- +---------------------------+--------------+
-- | region                    | difference   |
-- +---------------------------+--------------+
-- | Caribbean                 |    277703450 |
-- | Southern and Central Asia | 363457732030 |
-- | Central Africa            |   1107324225 |
-- | Southern Europe           |   5892084442 |
-- | Middle East               |   5447126026 |
-- | South America             |  48360987141 |
-- | Polynesia                 |       800125 |
-- | Australia and New Zealand |    286004264 |
-- | Western Europe            |  10585925902 |
-- | Eastern Africa            |   1537576934 |
-- | Western Africa            |   7496767968 |
-- | Eastern Europe            |  33347672284 |
-- | Central America           |  17179992036 |
-- | North America             |  77704892133 |
-- | Southeast Asia            |  31930949775 |
-- | Southern Africa           |   1768680808 |
-- | Eastern Asia              | 499404187466 |
-- | Nordic Countries          |    211622313 |
-- | Northern Africa           |   4133421486 |
-- | Baltic Countries          |     25696360 |
-- | Melanesia                 |      5987541 |
-- | Micronesia                |       822671 |
-- | British Islands           |   4813999886 |
-- +---------------------------+--------------+
-- 23 rows in set (0.0133 sec)


-- 3. Вывести десять языков, на которых разговаривает больше всего людей
select language 
	from countrylanguage 
	join country 
		on countrylanguage.countrycode = country.code
group by language
order by sum((population / 100) * percentage) desc
limit 10;


-- +------------+
-- | language   |
-- +------------+
-- | Chinese    |
-- | Hindi      |
-- | Spanish    |
-- | English    |
-- | Arabic     |
-- | Bengali    |
-- | Portuguese |
-- | Russian    |
-- | Japanese   |
-- | Punjabi    |
-- +------------+
-- 10 rows in set (0.0039 sec)


-- Запросы к таблицам схемы hospital

-- 4. Вывести названия специальностей и суммарное количество дней отпусков, 
-- в которых были врачи каждой специальности; отсортировать по возрастанию 
-- суммарного количества дней отпуска

select specializations.specialization as spec, sum(datediff(end_date, start_date)) as days
	from specializations 
	join specializations_doctors 
		on specializations_doctors.specializations_id = specializations.id
	join vacations
		on vacations.doctors_id = specializations_doctors.doctors_id
group by spec
order by days;

-- +-------------------+--------+
-- | spec              | days   |
-- +-------------------+--------+
-- | Кардиолог         |  28262 |
-- | Оториноларинголог |  37585 |
-- | Анестезиолог      |  41968 |
-- | Эндокринолог      |  54817 |
-- | Иммунолог         |  60994 |
-- | Стоматолог        |  69697 |
-- | Дерматолог        |  77071 |
-- | Онколог           |  78663 |
-- | Ортопед           |  91959 |
-- | Травматолог       | 106294 |
-- | Нарколог          | 115715 |
-- | Диетолог          | 131099 |
-- | Уролог            | 182896 |
-- | Реаниматолог      | 186337 |
-- | Хирург            | 203188 |
-- | Невролог          | 217197 |
-- | Офтальмолог       | 303211 |
-- +-------------------+--------+
-- 17 rows in set (0.0030 sec)


-- 5. Вывести округлённую до целого сумму средств, которую можно выделить на одну палату этого отделения 
-- (в зависимости от количества палат в отделении), от всех пожертвований каждому отделению; 
-- отсортировать по убыванию найденной суммы

select department,  round(sum(donations.amount) / count(distinct wards.ward, 2)) as `donation_per_ward`
from departments
join wards
on  departments.id = wards.departments_id
join donations
on donations.departments_id = departments.id
group by department
order by `donation_per_ward` desc;


select department,  round(sum(donations.amount) / count(distinct wards.ward)) as `donation_per_ward`, count(distinct wards.ward) as cou
from departments
join wards
on  departments.id = wards.departments_id
join donations
on donations.departments_id = departments.id
group by department
order by `donation_per_ward` / count(distinct wards.ward) desc;