--Триггер CLR для определения правильности заполнения столбца years_in
CREATE OR REPLACE FUNCTION CompareAgeYearsIn()
RETURNS TRIGGER
AS $$
	plan = plpy.prepare("SELECT age FROM Character where id_character = $1",["INT"])
	result = plpy.execute(plan, [TD["new"]["id_character"]])
	age_k = 0
	for x in result:
		age_k = x["age"]
	if TD["new"]["years_in"] < age_k:
		plpy.notice(f"{TD['new']['years_in']} years_in is okey!")
	else:
		plpy.notice(f"{TD['new']['years_in']} years_in not okey! !")
$$ LANGUAGE PLPYTHON3U;
CREATE TRIGGER NoticeAge AFTER INSERT ON organ_and_charac
FOR ROW EXECUTE PROCEDURE CompareAgeYearsIn();

INSERT INTO organ_and_charac(id_organization, id_character, state, years_in)
SELECT id_religion, id_character, alive, age + 30
FROM Character
WHERE id_character = 1398;