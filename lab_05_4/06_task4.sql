DROP table IF EXISTS temp;
create table temp(
data jsonb);

--Извлечь XML/JSON фрагмент из XML/JSON документа
copy temp(data) from '/data/religions_j.json';

--Извлечь значения конкретных узлов или атрибутов XML/JSON документа
select data->'name' from temp;

--Выполнить проверку существования узла или атрибута
DROP FUNCTION IF EXISTS if_key_exists;
CREATE FUNCTION if_key_exists(json_to_check jsonb, key text)
RETURNS BOOLEAN 
AS $$
BEGIN
    RETURN (json_to_check->key) IS NOT NULL;
END;
$$ LANGUAGE PLPGSQL;

SELECT if_key_exists('{"Id_religion": 15,"name": "Лев Ночи","type": "Генотеизм","clergy": "Не известно","propagation": "Йи Ти","followers": 4046}', 'name');

--Изменить XML/JSON документ
UPDATE temp SET data = data || '{"name": "Львы ночи"}'::jsonb 
where (data->'name')::VARCHAR = '"Лев Ночи"';

copy temp(data) from '/data/religions_j.json';

select data->'name' from temp;

--Разделить XML/JSON документ на несколько строк по узлам
SELECT *
FROM jsonb_array_elements
(
    '[
    {"type": "Монотеизм"},
    {"type": "Генотеизм"},
	{"type": "Священнослужители"}
    ]'
);