CREATE TABLE Dragons
(
	Id_dragon serial primary key NOT NULL,
	name varchar(40) NOT NULL,
	cur_master_id int NOT NULL,
    masters_id json,
    Foreign key (cur_master_id) references Character (Id_character)
);

COPY Dragons FROM '/data/dragons.json';

DROP PROCEDURE IF EXISTS ChangePersonStatus(id INT, n_alive BOOL);

CREATE OR REPLACE PROCEDURE ChangePersonStatus(id INT, n_id int)
AS $$
BEGIN 
	UPDATE Character
	SET id_house = n_id
	WHERE Character.id_character = id;
END;
$$ LANGUAGE PLPGSQL;