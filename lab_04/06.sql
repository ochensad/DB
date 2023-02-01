--Пользовательский тип данных для опеределения войны
DROP TYPE IF EXISTS war;
CREATE TYPE war AS (
    name_house_1 VARCHAR,
    name_house_2 VARCHAR,
    years INT,
    deaths INT
);
CREATE OR REPLACE FUNCTION SetWarInfo(nm_1 VARCHAR, nm_2 VARCHAR, years INT, deaths INT)
RETURNS SETOF war
AS $$
    return ([nm_1, nm_2, years, deaths],)
$$ LANGUAGE PLPYTHON3U;
SELECT * FROM SetWarInfo('Старки', 'Ланистеры', 2, 3000);