

CREATE FUNCTION GetKingInfo(id_c int)
RETURNS TABLE 
	(character_name VARCHAR,
	 king_name VARCHAR,
	 kingdom_id INT
	) AS $$
BEGIN 
	DROP TABLE IF EXISTS KING_STAT;
	CREATE TEMP TABLE KING_STAT(
	 character_name VARCHAR,
	 king_name VARCHAR,
	 kingdom_id INT	
	);
	 
	CREATE OR REPLACE VIEW Kings_v
	AS
	SELECT Character.name as k_name, House.id_kingdom
	 FROM Character JOIN House 
	 on Character.id_house = House.id_house where Character.title like '%Корол%';
	
	INSERT INTO KING_STAT(character_name, king_name, kingdom_id)
	select T1.name, Kings_v.k_name, T1.id_kingdom 
	from (SELECT Character.name, House.id_kingdom
	 FROM Character JOIN House 
	 on Character.id_house = House.id_house where Character.id_character = id_c) as T1
	 join Kings_v on Kings_v.id_kingdom = T1.id_kingdom where T1.id_kingdom = Kings_v.id_kingdom limit 1;
	
	
	 RETURN query SELECT * FROM KING_STAT;
END;
$$ LANGUAGE PLPGSQL;	


SELECT * FROM GetKingInfo(125);

