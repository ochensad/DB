-- Многооператорная табличная для вывода имени персонажа, имени организации и годах в ней
DROP FUNCTION IF EXISTS GetOrganizationInfo(int);

CREATE FUNCTION GetOrganizationInfo(id_c int)
RETURNS TABLE 
	(character_name VARCHAR,
	 organization_name VARCHAR,
	 year_in VARCHAR
	) AS $$
BEGIN 
	DROP TABLE IF EXISTS DETECTED_STAT;
	CREATE TEMP TABLE DETECTED_STAT(
	 character_name VARCHAR,
	 organization_name VARCHAR,
	 year_in VARCHAR	
	);
	INSERT INTO DETECTED_STAT(character_name, organization_name, year_in)
	SELECT T.name, Organization.name, T.years_in
	FROM Organization
		JOIN
	(SELECT Character.name, organ_and_charac.id_organization, organ_and_charac.years_in
	 FROM Character JOIN organ_and_charac 
	 on Character.id_character = organ_and_charac.id_character where Character.id_character = id_c) as T
	 on T.id_organization = Organization.id_organization;
	 
	 RETURN query SELECT * FROM DETECTED_STAT;
END;
$$ LANGUAGE PLPGSQL;	


SELECT * FROM GetOrganizationInfo(4);