DROP PROCEDURE IF EXISTS getDbMeta(dbname TEXT);

CREATE OR REPLACE PROCEDURE getDbMeta(dbname TEXT)
AS $$
	DECLARE 
		dbid int;
BEGIN
	SELECT pg_database.oid
		FROM pg_database
	WHERE pg_database.datname = dbname
	INTO dbid;
	RAISE NOTICE 'DB: %, ID: %', dbname, dbid;
END;
$$ LANGUAGE PLPGSQL;

CALL getDbMeta('Game_of_Thrones');