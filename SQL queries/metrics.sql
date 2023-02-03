CREATE DATABASE metrics;
USE metrics;

CREATE TABLE Personas (
persona_id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
task_id INT, -- FK from Tasks
minimum_target INT);

CREATE TABLE Pillars(
pillar_id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
pillar_name VARCHAR(30) NOT NULL UNIQUE
);


CREATE TABLE customer (  
  ID INT NOT NULL AUTO_INCREMENT,  
  Name varchar(50) NOT NULL,  
  City varchar(50) NOT NULL,  
  PRIMARY KEY (ID)  
);  

CREATE TABLE contact (  
  ID INT,  
  Customer_Id INT,  
  Customer_Info varchar(50) NOT NULL,  
  INDEX par_ind (Customer_Id),  
  CONSTRAINT fk_customer FOREIGN KEY (Customer_Id)  
  REFERENCES customer(ID)
  ON DELETE CASCADE  
  ON UPDATE CASCADE  
);  

CREATE TABLE Weights (
pillar_id INT, -- FK
persona_id INT, -- FK
PRIMARY KEY (pillar_id, persona_id),
weight DECIMAL(7,4)
);
ALTER TABLE Weights
ADD FOREIGN KEY (pillar_id) REFERENCES Pillars(pillar_id) ON DELETE CASCADE ON UPDATE CASCADE,
ADD FOREIGN KEY (persona_id) REFERENCES Personas(persona_id) ON DELETE CASCADE ON UPDATE CASCADE;
describe weights;
drop table weights;

CREATE TABLE Performance_itemised (
employee_id INT, -- FK from Employees
persona_id INT, -- CALC from Employees
actual_target INT NOT NULL,
minimum_target INT, -- CALC from Personas
target_met VARCHAR(5),
pillar_id INT); -- CALC from Tasks

CREATE TABLE Tasks (
task_id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
task_name VARCHAR(100) NOT NULL UNIQUE,
task_point INT,
pillar_id INT -- FK
);


SELECT * FROM Personas;
SELECT * FROM Performance_itemised;
SELECT * FROM Employees;
SELECT * FROM Weights;
SELECT * FROM Pillars;
SELECT * FROM Tasks;
DESCRIBE Personas;
DROP DATABASE metrics;