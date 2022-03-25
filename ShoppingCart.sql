create database shopping_cart;

use shopping_cart;

create table Addresses(
 id int primary key auto_increment,
 street varchar(30) not null,
 city varchar(20) not null,
 postcode varchar(10) not null);
 
 
 create table Items(
 id int primary key auto_increment,
 descrip varchar(100) default 'Description',
 price float(4,2) not null,
 name varchar(20) not null);
 
 
 create table Users(
 id int primary key auto_increment,
 username varchar(50) not null,
 user_id tinyint not null,
 email varchar(50),
 address_id int not null,
 item_id int not null,
 foreign key (address_id) references Addresses(id),
 foreign key (item_id) references Items(id));
 
 insert into Addresses values (1, 'London Street', 'Leeds', 'LS1 01A');
 
 select * from Addresses;
 select * from Items;
 select * from Users;
 
insert into Addresses(street, city, postcode) values ( 'High Street', 'London', 'NW03 01A');
  
insert into Addresses(street, city, postcode) values ( 'Rose Alley', 'Glasgow', 'GL01 01A'),
(  'St George\'s Road', 'Brighton', 'BN01 01A'); 


insert into Items(descrip, price, name) values ('super cool hat',9.55,'Hat'),('super cool magnifying glass',15.45,'magnifying glass'),('smoking stinks', 20.99, 'Pipe');

insert into Users values (1, 'sholmes', 12, 'sherlock@holmes.com', 1, 2 );
insert into Users values (2, 'watson', 12, 'watson@holmes.com', 2, 2 );

-- this one will give an error
update Items set descrip = 'hyper cool magnifying glass' where price = 9.55;

select * from Items where id = 2;

select price, descrip, name from Items where id = 1;

select name, descrip as 'description', price * 0.2 as 'tax' from Items;

select concat(street,' ', city) as 'Full Address' from Addresses;

insert into Items(descrip, price, name) values ('Walking Stick',9.55,'Stick');

select distinct price from Items;

select * from Items order by price,name asc;

select username, email, street, city, postcode from Users inner join Addresses on Users.address_id = Addresses.id where Users.id = 1;

select username, price, descrip as 'description', name as 'item_name' from Users right outer join Items on Users.item_id = Items.id;

select * from Items where id >= 2;

select * from Items where price between 10.00 and 20.00;

