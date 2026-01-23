Create database Cartoon;
Use Cartoon;
create table Doraemon(
		ID int,
        name char,
        address varchar(100),
        age int
        );

drop table doraemon;

-- Constraints -> CONDITIONS
-- while creating table
-- SYNTAX: 
-- create table table_name(
		-- col_1 datatype constraint,
        -- col_2 datatype constraint,
       --  );
-- Contraint 1 -> Not NULL
create table Doraemon(
		ID int not null,
        name char,
        address varchar(100),
        age int
        );
alter table doraemon
modify column name char not null;
-- Contraint 2 -> UNIQUE 
		  --   -> Can be NULL

alter table doraemon
modify column address varchar(100) unique;
alter table doraemon
modify column age int not null unique; -- two constraints can be used together

create table shinchan(
		ID int not null,
        name char,
        address varchar(100),
        age int,
        unique(address,name)
        );
        
-- Primary Key -> NOT NULL + UNIQUE
-- Single PK
alter table shinchan
add primary key(ID);

-- Multiple PK
alter table doraemon
add constraint doraPR primary key(id,name,address);

drop table shinchan;
drop table doraemon;


-- DATA -> Rows

create table employee(
		id int,
        name char not null,
        salary int not null,
        experience int not null,
        primary key(id));
alter table employee
modify column name char(50);

-- Insert into -> inserting data
-- SYNTAX: 
-- 		insert into table_name(col_1,col_2....)
-- 		values (1,'EXAM','abc@abc.abc)

insert into employee(id,name,salary,experience)
values (01,'Shri',100000,5);
insert into employee(id,name,salary,experience)
values (02,'Rahul',20000,2);
insert into employee(id,name,salary,experience)
values (03,'Rohit',50000,1);
insert into employee(id,name,salary,experience)
values (04,'Virat',75000,10);

insert into employee() -- no need to mention each col name
values(05,'Loki',120000,3); -- useful when each field data has been given

-- insert into employee(id,name) -> cannot work as salary and experience is set to not null
-- values(06,'Huma')

-- select everything from the table
select * from employee;
-- select few
select id,name from employee;
select id,salary from employee;
select Name,Salary from employee;
select name,Salary from employee; #heading is case sensitive

insert into employee()
values(06,'Neha',100000,5);
select * from employee;
select distinct salary from employee; -- 100000 repeated twice is not printed

select salary from employee
where salary>50000;
select *  from employee
where salary>50000;
-- operators -> <,>,<=,>=,=,between,like(specifies a pattern) & != or <> -> not equal to
--           -> and, or & not operators

-- Update function
-- SYNTAX:
-- update table_name
-- set col_2 data = "data"
-- where col_2 = 01;

update employee
set name='Thor'
where id = 5;

use cartoon;
select * from employee;

-- deleting a data
-- SYNTAX:
-- delete from table_name
-- where criteria
set sql_safe_updates=0;
delete from employee
where salary<75000; 
select * from employee;

-- soft delete -> deletes data for the user, but saved in the back end 
-- hard delete -> completely destroys the data



















        

