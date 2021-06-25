====================== CREATE KEYSPACE ==========================
CREATE KEYSPACE FirstKeyspace 
WITH replication = {'class': 'SimpleStrategy', 
'replication_factor': '1'};
DESCRIBE keyspaces;
USE FirstKeyspace;

====================== CREATE TABLE ============================
CREATE TABLE emp(
 emp_id int,
 emp_name text,
 emp_age int,
 PRIMARY KEY((emp_id))
 );

====================== INSERT VALUES ==========================
INSERT INTO emp (emp_id, emp_name, emp_age)
VALUES(20,'mikel', 30);
INSERT INTO emp (emp_id, emp_name, emp_age)
VALUES(10,'john', 28);

====================== UPDATE VALUES ==========================
UPDATE emp SET emp_age=31 WHERE emp_id=10;

====================== READ VALUES ==========================
select * from emp where emp_id=10;
# where uslov se moze koristiti samo nad kolonama koje su deo kljuca
select * from emp where emp_name='john';

====================== DELETE VALUES ==========================
delete from emp where emp_id=10;
truncate table emp;

====================== DROP ==========================
DROP TABLE emp;
DROP KEYSPACE FirstKeyspace;