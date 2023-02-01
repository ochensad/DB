DROP FUNCTION IF EXISTS GetAvgCastelsPopulation(INT);

--Скалярная функция для вывода среднего населения в закмах королевства.
CREATE OR REPLACE FUNCTION GetAvgCastelsPopulation(id INT)
RETURNS INT AS $$
BEGIN
	RETURN (SELECT AVG(population) FROM Castle WHERE id_kingdom = id and type = 'Замок');
END;
$$ LANGUAGE PLPGSQL;

SELECT name, GetAvgCastelsPopulation(id_kingdom)
FROM Kingdom;