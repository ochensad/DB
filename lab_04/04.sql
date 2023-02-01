--Хранимая процедура CLR для обновления возраста персонажа
CREATE EXTENSION IF NOT EXISTS plpython3u;
DROP PROCEDURE IF EXISTS ChangePersonAge;
CREATE OR REPLACE PROCEDURE ChangePersonAge(id INT, n_age_change INT)
AS $$
	plan = plpy.prepare("UPDATE Character SET age = age + $1 WHERE Character.id_character = $2;",["INT", "INT"])
	plpy.execute(plan, [n_age_change, id])
$$ LANGUAGE PLPYTHON3U;

select * from character where id_character = 4;
CALL ChangePersonAge(4, 2);
select * from character where id_character = 4;