--Хранимая процедура с параметрами для обновления статуса персонажа
DROP PROCEDURE IF EXISTS ChangePersonStatus(id INT, n_alive BOOL);

CREATE OR REPLACE PROCEDURE ChangePersonStatus(id INT, n_alive BOOL)
AS $$
BEGIN 
	UPDATE Character
	SET alive = n_alive
	WHERE Character.id_character = id;
END;
$$ LANGUAGE PLPGSQL;


CALL ChangePersonStatus(4, false);
select * from character where id_character = 4;