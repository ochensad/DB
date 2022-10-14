--Лабораторная работа №2
-- SQL запросы


--Инструкция SELECT, использующая предикат сравнения.
-- Вывести все замки, в которых живет больше 900 людей.
SELECT id_castle, name, population FROM Castle WHERE population > 900;

--Инструкция SELECT, использующая предикат BETWEEN.
--Вывести всех персонажей, которые считаются молодежью.
SELECT id_character, name, age FROM Character WHERE age BETWEEN 14 AND 35;

--Инструкция SELECT, использующая предикат LIKE.
--Вывести id тех персонажей, у которых на гербе дома медведь
SELECT DISTINCT id_character, blazon
FROM Character JOIN House ON character.id_house = House.id_house
WHERE blazon LIKE '%едведь%';

--Инструкция использующая предикат IN с вложенным подзапросом.
--Вывести персонажей, которые входят в организацию 1 и имеют мужской пол
SELECT * FROM Character
WHERE id_character IN (SELECT id_character 
			 FROM organ_and_charac 
			 WHERE id_organization = 1 AND state = True)
         AND 
		 sex = 'м'; 

--Инструкция SELECT, использующая предикат EXISTS с вложенным подзапросом.
--Вывести информацию об королевствах, в которых тип Замок и население больше 1000 
SELECT * FROM Kingdom WHERE EXISTS
(SELECT id_kingdom FROM Castle WHERE type = 'Замок' and population > 1000);

-- Инструкция SELECT, использующая предикат сравнения с квантором.
--Вывести информацию о религиях, тип которых Монотеизм и количество последователей которой меньше населения любого Королевства в Вестеросе
SELECT * FROM Religion
WHERE type = 'Монотеизм'
AND
followers < ALL(SELECT population FROM Kingdom WHERE location = 'Вестерос');

-- Инструкция SELECT, использующая агрегатные функции в выражениях столбцов.
--Вывести среднее количество населения в замках на Севере
SELECT AVG(population) AS AVG_POPYLATION 
FROM Castle WHERE id_kingdom = (SELECT id_kingdom 
			 FROM Kingdom 
			 WHERE name = 'Север');

--Инструкция SELECT, использующая скалярные подзапросы в выражениях столбцов.
--Вывести имя, пол, возраст и средний возраст всех Валирийцев
SELECT name, sex, age ,(SELECT AVG(age) FROM Character ) as avg_age
FROM Character WHERE culture = 'Валирийцы';

--Инструкция SELECT, использующая простое выражение CASE
--Вывести все религии, если деховенство "Не известно" заменить на 
--"Священнослужители"
SELECT id_religion, name,
CASE 
WHEN clergy = 'Не известно' THEN ('Священнослужители')
ELSE CAST (clergy as VARCHAR)
END clergy
FROM Religion;

--Инструкция SELECT, использующая поисковое выражение CASE.
--Вывести название организации и уровень ее угрозы
SELECT id_organization, name, 
CASE
WHEN followers < 50 THEN 'Незначительна'
WHEN followers < 200 THEN 'Имеет небольшое влияние в регионе'
WHEN followers < 400 THEN 'Достаточно опасна'
ELSE 'Может уничтожить армию'
END danger
FROM Organization;

--Создание новой временной локальной таблицы из результирующего набора данных инструкции SELECT
--Создания временной локальной таблицы с всеми живыми персонажами мужского пола
CREATE TEMP TABLE Alive_man_characters AS
SELECT id_character, name, sex, age, alive 
FROM Character
WHERE alive = true and sex = 'м';
select * from Alive_man_characters;

--Инструкция SELECT, использующая вложенные коррелированные
--подзапросы в качестве производных таблиц в предложении FROM
--Выбрать всех персонажей, которые живут дольше, чем некоторые служат в
--какой-либо организации
SELECT id_character, name, sex, age 
FROM Character 
WHERE age > (
	SELECT MAX(years_in) 
	FROM organ_and_charac
	WHERE state = True);

--Инструкция SELECT, использующая вложенные подзапросы с уровнем вложенности 3
--Вывести все организации в которые входят персонажи, которые живы и, дома которых находятся в Просторе
SELECT id_organization, name FROM Organization WHERE id_organization IN 
	(SELECT id_organization FROM organ_and_charac WHERE state = True AND id_character IN
		(SELECT id_character FROM Character WHERE alive = true and id_house IN
			(SELECT id_house FROM House WHERE id_kingdom IN (
        SELECT id_kingdom FROM Kingdom where name = 'Простор'
      ))
		 )
	 );


-- Инструкция SELECT, консолидирующая данные с помощью предложения GROUP BY, но без предложения HAVING
--Вывести типы замков с их количеством и средним возрастом
SELECT type, COUNT(type) AS qty_type, AVG(age) as avg_age FROM Castle
GROUP BY type;

--Инструкция SELECT, консолидирующая данные с помощью предложения GROUP BY и предложения HAVING
--Вывести id Королевств с количеством замков в них, и их средним возрастом, где их больше 10
SELECT id_kingdom, COUNT(id_kingdom) AS qty_castles, AVG(age) as avg_age FROM Castle
GROUP BY id_kingdom
HAVING COUNT(id_kingdom) > 10;


--Однострочная инструкция INSERT, выполняющая вставку в таблицу одной строки значений
--Вставка Королевства
INSERT INTO Kingdom(id_kingdom, name, main_river, location, population, exist)
VALUES(26, 'Незведанные земли', 'Закатное море', 'Общие земли', 0, True);

--Многострочная инструкция INSERT, выполняющая вставку в таблицу
--результирующего набора данных вложенного подзапроса
--Вставить новую связь организации и персонажа
INSERT INTO organ_and_charac(id_organization, id_character, state, years_in)
SELECT id_religion, id_character, alive, age - 10
FROM Character
WHERE id_character = 1402;

--Простая инструкция UPDATE
--Апдейт религии
UPDATE Religion
SET followers = 60000
WHERE followers > 40000 AND followers < 60000;
SELECT * FROM Religion;

--Инструкция UPDATE со скалярным подзапросом в предложении SET
--Обноваить в новом королевстве население
UPDATE Kingdom
SET population = (SELECT AVG(population) FROM Kingdom)
WHERE id_kingdom > 25;

--Простая инструкция DELETE
--Удалить последнее королевство
DELETE FROM Kingdom
WHERE id_kingdom = 26;


--Инструкция DELETE с вложенным коррелированным подзапросом в предложении WHERE
--Удалить организации из связей, где кол-во людей в организации меньше среднего
DELETE FROM organ_and_charac
WHERE id_organization IN
(SELECT id_organization FROM Organization WHERE followers < (
  SELECT AVG(followers) FROM Organization));


--Инструкция SELECT, использующая простое обобщенное табличное выражение
--Среднее население по всем королевствам
WITH CTE (id, population_n) AS
	(SELECT id_kingdom, population
	FROM Kingdom
	GROUP BY id_kingdom)
SELECT AVG(population_n) as AVG_POPYLATION
FROM CTE;


--Инструкция SELECT, использующая рекурсивное обобщенное табличное выражение.
--Умножение на 5
WITH RECURSIVE MUL5(N) AS
(SELECT 5 
UNION ALL 
SELECT N+5 FROM MUL5
WHERE N < 10000)
SELECT N FROM MUL5;

--Оконные функции. Использование конструкций MIN/MAX/AVG OVER()
--Организации и средние года в них
SELECT DISTINCT id_organization, AVG(years_in) OVER (PARTITION BY id_organization)  as AVG_Years FROM organ_and_charac;

--Оконные функции для устранения дублей
--Создаем копии персонажей и выводим только первый ряд
WITH double AS
((SELECT c.id_character, c.name FROM character c)
 
 UNION ALL 
 
(SELECT c.id_character, c.name FROM character c)
 ORDER BY id_character
)

SELECT id_character, name FROM
(SELECT id_character, name, ROW_NUMBER() OVER (PARTITION BY id_character, name) AS rn 
 FROM double) as dbl
WHERE dbl.rn = 1
ORDER BY id_character;