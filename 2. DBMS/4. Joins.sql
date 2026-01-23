create database sports;
use sports;
create table cricket(

	player_ID int auto_increment,
    player_name char(100) not null,
    player_role char(100) not null,
    country char(100) not null,
    primary key(player_id));
insert into cricket(player_name,player_role,country)
values
('Dhoni','Wk','India'),
('Kohli','Bat','India'),
('Stokes','All Rounder','England'),
('Starc','Ball','Australia'),
('Buttler','Wk','England'),
('Williamson','Bat','New Zealand'),
('Pollard','AllRounder','West Indies'),
('Bumrah','Ball','India'),
('Rashid','Ball','Afghanistan'),
('Smith','Bat','Australia'),
('ABD','Bat','South Africa');
select * from cricket;
select player_role from cricket;

create table football(

	player_ID int auto_increment,
    player_name char(100) not null,
    player_role char(100) not null,
    country char(100) not null,
    primary key(player_id));
insert into football(player_name,player_role,country)
values
('Messi','Forward','Argentina'),
('Ronaldo','Forward','Portugal'),
('Neymar','Left Wing','Brazil'),
('Pogba','Centre','France'),
('Lloris','Goalie','France');
select * from football;

-- aliases -> short form for a field name
select player_role as PR
from cricket;

select * from football
where player_id > 2;
drop database sports;

create database company;
use company;


create table employee(
		EID int auto_increment,
        ENAME char(100) not null,
        city char(100) not null,
        primary key(EID));

create table department(
		DID int auto_increment,
        Dname char(100) not null,
        EID int,
        primary key(DID));
        
insert into employee(ename,city)
values
('Shri','Bengaluru'),
('Rajesh','Mumbai'),
('Babu','Jammu'),
('ROshan','Hyderabad'),
('Wahid','Durgapur'),
('Ashlesha','Mumbai'),
('Navin','Vizag'),
('Shubham','Chennai'),
('Vivek','Kolhapur'),
('Arnold','Bengaluru');

 insert into department(DNAME,EID)
 values
 ('HR',5),
 ('RnD',7),
 ('IT',10),
 ('Sales',1),
 ('Finance',12),
 ('Production',8),
 ('QnA',14),
 ('Acounts',2),
 ('Public Relations',9),
 ('Purchases',6);
 
 -- INNER JOIN 
 -- SYNTAX:
 -- select col_name(s)
 -- from table_1
 -- inner join table_2
 -- on table_1.col_name=table_2.col_name; -> related/equal columns
 
 select * from employee
 inner join department
 on employee.EID=department.eid; -- the two tables have been combined
 
 -- OUTER JOIN -> Union values
 -- Left Outer -> Entire T1+Intersection
 
 select * from employee
 left join department
 on employee.eid=department.eid;
 
 select ename,city,dname from employee
 left join department
 on employee.eid=department.eid
 where city='mumbai';
 
-- Right outer -> all data from right table and intersection values
 select * from employee
 right join department
 on employee.eid=department.eid;
 
 select employee.eid,employee.ename,employee.city,department.dname from employee
 right join department
 on employee.eid=department.eid
 where city='Bengaluru'
 order by eid;
 
 -- Full Outer -> Data from T1, data from T2 abd the matching values
 -- Full outer does not directly work in MySQL workbench
 -- We need to do union of left and right outer
 select * from employee 
 left join department
 on employee.eid=department.eid
 union -- to combine left and right outer
 select * from employee 
 right join department
 on employee.eid=department.eid;
 
 select employee.eid,city,employee.ename,department.dname from employee
 left join department
 on employee.eid=department.eid
 union 
 select employee.eid,city,employee.ename,department.dname from employee
 right join department
 on employee.eid=department.eid;
 
 select * from department
 left join employee
 on department.eid=employee.eid
 union 
 select * from department
 right join employee
 on department.eid=employee.eid; -- during union, priority is given to first part 
 
 select ename,eid from employee
 union 
 select did,dname from department;
 
 -- UNION ALL -> Shows all the data,, INCLUDING repeated values... allows duplication
 