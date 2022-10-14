COPY Religion FROM '/data/religions.csv' DELIMITER ';' CSV HEADER;
COPY Kingdom FROM '/data/kindoms.csv' DELIMITER ';' CSV HEADER;
COPY Organization FROM '/data/organizations.csv' DELIMITER ';' CSV HEADER;
COPY House FROM '/data/houses.csv' DELIMITER ';' CSV HEADER;
COPY Castle FROM '/data/castels.csv' DELIMITER ';' CSV HEADER;
COPY Character FROM '/data/persons.csv' DELIMITER ';' CSV HEADER;
COPY Organ_and_charac FROM '/data/organizations_and_persons.csv' DELIMITER ';' CSV HEADER;