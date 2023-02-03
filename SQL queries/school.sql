CREATE DATABASE school;
USE school;

CREATE TABLE teacher (
teacher_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
first_name VARCHAR(40) NOT NULL,
last_name VARCHAR(40) NOT NULL,
language_1 VARCHAR(3) NOT NULL,
language_2 VARCHAR(3),
dob DATE,
tax_id INT UNIQUE,
phone_no VARCHAR(20),
CONSTRAINT CHK_data CHECK (tax_id>=0 AND last_name<>'Mammadov')
);
INSERT INTO teacher(first_name, last_name, language_1, language_2, dob, tax_id, phone_no) VALUES ('James', 'Smith', 'ENG', NULL, '1985-04-20', 72345, '+491774553676'), ('Stefanie', 'Stefanie', 'FRA', NULL, '1970-02-17', 63456, '+491234567890');
INSERT INTO teacher VALUES (8, 'James', 'Smith', 'ENG', NULL, '1985-04-20', 12335, '+491774553676'), (10, 'Stefanie', 'Stefanie', 'FRA', NULL, '1970-02-17', 33456, '+491234567890');
SELECT * FROM teacher;
SHOW INDEXES from teacher;
SHOW TABLES;
SHOW DATABASES;
DESCRIBE teacher;
DROP TABLE teacher;

SELECT language_1, SUM(tax_id) as tax_by_language FROM teacher GROUP BY language_1;
SELECT first_name, last_name, dob FROM teacher;
SELECT DISTINCT language_1 FROM teacher ORDER BY language_1;
SELECT * FROM teacher WHERE language_1 = "ENG" AND language_2 = "IRI";
SELECT * FROM teacher WHERE language_1 IN ("ENG", "RUS");
SELECT * FROM teacher WHERE language_1 NOT IN ("ENG", "RUS");
SELECT * FROM teacher WHERE language_1 LIKE "E%";
SELECT * FROM teacher WHERE language_1 LIKE "%E";
SELECT * FROM teacher WHERE language_1 LIKE "%E%";
SELECT * FROM teacher WHERE language_1 LIKE "E__";
SELECT * FROM teacher ORDER BY first_name DESC;
SELECT * FROM teacher LIMIT 3;
INSERT INTO teacher VALUES (10, 'Lol', 'Lolikov', 'RUS', 'AZE', '1982-01-01', 58789, '+447911188991');
DELETE FROM teacher WHERE teacher_id = 10;
ALTER TABLE teacher DROP COLUMN email;
ALTER TABLE teacher ADD email varchar(255);
DROP TABLE participant;
DROP DATABASE school;
CREATE VIEW teachers_view AS SELECT first_name, language_1 FROM teacher WHERE language_1 = "ENG";
SELECT * FROM teachers_view;

SELECT first_name, language_2,
CASE
	WHEN language_2 IS NULL THEN "No language"
	ELSE language_2
END AS language_2
FROM teacher;

SELECT client_name FROM client 
WHERE EXISTS (SELECT * FROM course WHERE course.client = client.client_id AND language = 'ENG');

SELECT language FROM course
UNION
SELECT language_1 FROM teacher
UNION
SELECT language_2 FROM teacher
ORDER BY language;

create table sales(id int, amount int);
insert into sales(id,amount) values(1, 100),(4,300),(6,400);
select * from sales;
ALTER TABLE sales MODIFY id INT NOT NULL AUTO_INCREMENT PRIMARY KEY;
alter table sales AUTO_INCREMENT=100;
insert into sales(amount) values(512),(175);
select * from sales;
CREATE INDEX ind_1 ON sales(amount);
select * from sales;
SHOW INDEXES from sales;
-- ALTER TABLE sales DROP PRIMARY KEY;
-- ALTER TABLE sales DROP CONSTRAINT 'id';
DROP INDEX `PRIMARY` ON sales;
drop table sales;
