create database university;
use university;
create table compsc(
		id int,
        name char(100) not null,
        age int not null,
        email varchar(50) not null,
        marks int not null,
        primary key(ID));
alter table compsc
modify column age int;
alter table compsc
modify column marks float not null;
alter table compsc
modify column email varchar(50) unique;

insert into compsc()
values 
(1,'Shri',19,'shri@gmail.com',92.5),
(2,'Rahul',22,'rahul@gmail.com',65.5),
(3,'Ravi',23,'ravi@gmail.com',45.9); #need not write insert into multiple times

drop table compsc;

-- auto increment -> automatically increment by 1.... works only for primary key
create table compsc(
		id int auto_increment, -- automatically increment the values by 1
        name char(100) not null,
        age int,
        email varchar(50) unique,
        marks float not null,
        primary key(ID));
insert into compsc(name,age,email,marks)
values 
('Shri',19,'shri@gmail.com',92.5),
('Rahul',22,'rahul@gmail.com',65.5),
('Ravi',23,'ravi@gmail.com',45.9);
select * from compsc;

select * from compsc 
where marks>=60;

-- order by  -> sort
-- SYNTAX:
-- select col (or *)
-- from table_name
-- order by col_name

select marks
from compsc
order by name; #ascending order of names

select name
from compsc
order by marks desc; #descending order of marks

select *
from compsc
order by name desc;

insert into compsc(name,age,email,marks)
values
('Reshma',21,'reshma@gmail.com',98),
('Dinesh',18,'dinesh@gmail.com',52),
('Harish',22,'harish@gmail.com',67),
('Sahil',25,'sahil@gmail.com',69);

select * 
from compsc
order by age,name; -- if first field have identical values, check second field

select * 
from compsc
order by age desc, name asc; -- asc/desc in mixed way 
							 -- after specifying desc for age, we need to specify asc for name, ekse it'll be desc

-- MAX & MIN
-- SYNTAX:
-- select max/min(col_name)
-- from table_name;

select min(marks)
from compsc;

select min(marks)
from compsc
where marks>70; -- minimum after 70

select min(name)
from compsc; -- according to ascii values

-- COUNT 
-- SYNTAX:
-- select count(col_name)
-- from table_name;

select count(age)
from compsc; -- no. of different age counts

select count(marks)
from compsc
where marks>65;

-- AVG -> Average
-- SYNTAX:
-- select avg(col_name)
-- from table_name;
select avg(marks)
from compsc;

select avg(marks)
from compsc
where age>=22; -- avg of ppl over 21yrs

select avg(age)
from compsc
where marks>65; -- avg age of ppl with marks greater than 65

select avg(age)
from compsc
where marks>100; -- returns the answer NULL -> no values 

-- SUM -> Sum over all values
select sum(marks)
from compsc; #sum of all marks

select sum(age)
from compsc
where marks>65;

select sum(marks)
from compsc 
where marks<80 and age>20;

-- BETWEEN 
select * from compsc
where marks between 60 and 80; -- includes end points also

select * from compsc
where marks not between 60 and 90;

insert into compsc(name,age,email,marks)
values
('Ramesh',22,'ramesh@yahoo.com',48),
('Suresh',28,'suresh@hotmail.com',92),
('Akash',25,'akash@rediffmail.com',87),
('Gohil',17,'gohil@linkedin.com',49);
select * from compsc;

-- like operator
-- SYNTAX:
-- select col_name from table_name
-- where col_name like '%pattern%';

select * from compsc
where email like '%gmail%';

-- starting with the pattern -> 'pattern%'
-- ending with the pattern -> '%pattern'
-- pattern at any position -> '%pattern%'
-- particular positon -> '___....._pattern%' no.of _ -> nth position
-- starting and ending -> 'p%q' -> starting p and ending q

select * from compsc
where name like '%h';
select * from compsc
where name like 'r%a';




 
