--Определяемая пользователем табличная функция CLR для вывода общей информации
-- о персонаже
CREATE EXTENSION IF NOT EXISTS plpython3u;
DROP FUNCTION IF EXISTS GetCharacterMainInfo;
create or replace function GetCharacterMainInfo(id int)
RETURNS TABLE(
	name VARCHAR,
	house VARCHAR,
    house_kingdom VARCHAR,
	motherland VARCHAR
) AS $$
	quest = "select T1.name, T1.h_name, Kingdom.name as k_name, T1.motherland \
from (SELECT Character.name, Character.motherland ,House.name as h_name ,House.id_kingdom \
FROM Character JOIN House  \
on Character.id_house = House.id_house where Character.id_character = $1) as T1 \
join Kingdom on Kingdom.id_kingdom = T1.id_kingdom where T1.id_kingdom = Kingdom.id_kingdom"
	plan = plpy.prepare(quest, ["INT"])
	result = plpy.execute(plan, [id])
	for x in result:
		yield(x["name"], x["h_name"], x["k_name"], x["motherland"])
$$ LANGUAGE PLPYTHON3U;

SELECT * from GetCharacterMainInfo(125);