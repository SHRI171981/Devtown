-- Create a database
-- SYNTAX : Create Database database_name;
create database test;


-- Delete a database
-- SYNTAX : Drop Database database_name;
drop database test; -- not used usually

-- Use a database
-- SYNTAX : Use database_name;
use test; -- select the test database


-- Create a table
-- SYNTAX : Create table table_name(
--        col_1 datatype_1,
--        col_2 datatype_2,
--        col_n datatype_n);
create table employee(
           name char(10), -- only characters and 10 is the limit
           salary int,
           department char,
           phone int(10),
           email varchar(100)); -- int char and symbols... Always needs a limit
           
-- create new table from existing table
-- SYNTAX: create table new_table_name as
-- 					select col_1,col_2 ... col_n
-- 					from existing_table_name;

create table employee1 as
		select salary,department
        from employee; 

-- deleting a table
-- 1. DROP
-- SYNTAX: drop table table_name; 
drop table employee; -- deletes entire table

-- 2. TRUNCATE
-- SYNTAX: truncate table table_name;
truncate table employee1; -- deletes only data inside table, not table itself


-- Updation of a table
-- 1. Adding a column
-- SYNTAX: alter table table_name
		-- add col_name datatype(n);
alter table employee
add marital_status char;

-- 2.Deleting a column
-- SYNTAX: alter table table_name
		-- drop col_name;
alter table employee
drop marital_status;
	
-- 3. Change data type of a column
-- SYNTAX: alter table table_name
		-- modify column col_name datatype;
alter table employee
modify column salary float;


        
        



