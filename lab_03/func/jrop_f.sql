DROP FUNCTION IF EXISTS GetAlivePersons(INT);

--Подставляемая функция для получения всех живых персонажей заданного возраста.
CREATE OR REPLACE FUNCTION GetAlivePersons(m_age INT = 20)
RETURNS TABLE (name TEXT, age INT, alive BOOL) 
AS'
	SELECT name, age, alive FROM Character WHERE age = m_age AND alive = true;
'
LANGUAGE SQL;

SELECT * from GetAlivePersons();