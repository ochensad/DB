--Хранимая процедура с курсором для вывода всех замков дома
DROP PROCEDURE IF EXISTS GetCastelsForHouse(id INT);

CREATE OR REPLACE PROCEDURE GetCastelsForHouse(id INT)
AS $$
DECLARE
	cname text;
	name_cur CURSOR for
		SELECT name FROM (SELECT c.name FROM Castle c JOIN House h on h.id_house = c.id_house
						    WHERE h.id_house = id) as ds;
BEGIN
	OPEN name_cur;
	LOOP
	FETCH name_cur INTO cname;
	EXIT WHEN NOT FOUND;
	RAISE NOTICE 'NAME OF CASTLE: %', cname;
	END LOOP;
	CLOSE name_cur;
END;
$$ LANGUAGE PLPGSQL;

CALL GetCastelsForHouse(4);