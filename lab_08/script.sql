create schema nifi_test

create table nifi_test.test_table
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
)

select * from nifi_test.test_table