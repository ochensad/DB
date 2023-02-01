DROP TRIGGER IF EXISTS AFTER_UPDATE_OAC on organ_and_charac;

DROP FUNCTION IF EXISTS OAC_UPDATE_INFO();

CREATE OR REPLACE FUNCTION OAC_UPDATE_INFO()
RETURNS trigger
AS $$
BEGIN
    RAISE NOTICE 'The OAC has been updated';

    RETURN NEW;
END;
$$ LANGUAGE PLPGSQL;

CREATE TRIGGER AFTER_UPDATE_OAC
AFTER UPDATE
on organ_and_charac
FOR EACH ROW
EXECUTE PROCEDURE OAC_UPDATE_INFO();

UPDATE organ_and_charac 
	SET state = true
	WHERE organ_and_charac.id_character = 82 and organ_and_charac.id_organization = 34;