--Скалярная функция для получения всех жителей, проживающих в замках n-го королевства
CREATE EXTENSION IF NOT EXISTS plpython3u;
DROP FUNCTION IF EXISTS GetCastlePopulation;
create or replace function GetCastlePopulation(n integer)
RETURNS DECIMAL
AS $$
	plan = plpy.prepare("select SUM(population) from Castle where id_kingdom = $1;", ["INT"])
	result = plpy.execute(plan, [n])
	qsum = 0
	qlen = len(result)
	if qlen == 0:
		return 0
	for x in result:
		qsum = x["sum"]
	return qsum
$$ LANGUAGE PLPYTHON3U;

SELECT name, population, GetCastlePopulation(id_kingdom) from Kingdom;