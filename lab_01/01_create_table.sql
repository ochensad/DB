-- Database: Game_of_Thrones

-- DROP DATABASE IF EXISTS Game_of_Thrones;

drop table if exists Organ_and_charac, Character, Castle, House, Organization, Kingdom, Religion;

	
CREATE TABLE Religion
(
	Id_religion serial primary key NOT NULL,
	name varchar(40) NOT NULL,
	type varchar(40) NOT NULL,
	clergy varchar(40) NOT NULL,
	propagation varchar(40) NOT NULL,
	followers int NOT NULL
);


	
CREATE TABLE Kingdom
(
	Id_kingdom serial primary key NOT NULL,
	name varchar(40) NOT NULL,
	main_river varchar(40) NOT NULL,
	location varchar(40) NOT NULL,
	population int NOT NULL,
	exist BOOLEAN NOT NULL
);



CREATE TABLE Organization
(
	Id_organization serial primary key NOT NULL,
	name varchar(40) NOT NULL,
	type varchar(40) NOT NULL,
	location varchar(40) NOT NULL,
	state varchar(40) NOT NULL,
	followers int NOT NULL
);

CREATE TABLE House
(
	Id_house serial primary key NOT NULL,
	name varchar(40) NOT NULL, 
	blazon varchar(100) NOT NULL,
	motto varchar(100) NOT NULL,
	followers int NOT NULL,
	exist BOOLEAN NOT NULL, 
	Id_kingdom int NOT NULL,
	Foreign key (Id_kingdom) references Kingdom (Id_kingdom)
	
);

CREATE TABLE Castle
(
	Id_castle serial primary key NOT NULL,
	name varchar(40) NOT NULL,
	type varchar(100) NOT NULL,
	population int NOT NULL,
	age int NOT NULL,
	Id_house int NOT NULL,
	Id_religion int NOT NULL,
	Id_kingdom int NOT NULL,
	FOREIGN KEY (Id_religion) REFERENCES Religion(Id_religion),
	FOREIGN KEY (Id_kingdom) REFERENCES Kingdom(Id_kingdom),
	FOREIGN KEY (Id_house) REFERENCES House(Id_house)
);

CREATE TABLE Character
(
	Id_character serial primary key NOT NULL,
	name varchar(40) NOT NULL,
	sex varchar(10) NOT NULL,
	culture varchar(40) NOT NULL,
	title varchar(200) NOT NULL,
	motherland varchar(100) NOT NULL,
	age int NOT NULL,
	alive BOOLEAN NOT NULL,
	Id_religion int NOT NULL,
	Id_house int NOT NULL,
	FOREIGN KEY (Id_religion) REFERENCES Religion(Id_religion),
	FOREIGN KEY (Id_house) REFERENCES House(Id_house)
);


CREATE TABLE Organ_and_charac
(
	Id_organization int NOT NULL,
	Id_character int NOT NULL,
	state BOOLEAN NOT NULL,
	years_in int NOT NULL,
	PRIMARY KEY (Id_organization, Id_character),
	foreign key (Id_organization) references Organization(Id_organization),
	foreign key (Id_character) references Character(Id_character)
	
);

