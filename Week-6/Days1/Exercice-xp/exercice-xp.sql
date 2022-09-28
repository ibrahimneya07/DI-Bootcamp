create table items(
	items_id serial primary key,
	item varchar(50) not null,
	prices integer not null
);
create table customers(
	customers_id serial primary key,
	first_name varchar(50) not null,
	last_name varchar(50) not null
);

insert into items(item,prices)
values(' Petit bureau',100),
		(' Grand bureau',300),
		(' Ventilateur',80);
insert into customers(first_name,last_name)
values('Greg','Jones'),
		('Sandra','Jones'),
		('Scott','Scott'),
		('Trevor','Vert'),
		('Mélanie','Johnson');
select *from items;
select *from customers;
select item from items where prices>80;
select item from items where prices<300;
select *from customers where last_name='Smith';--pas de last_name Smith dans la table des clients--
select *from customers where last_name='Jones';
select *from customers where not(last_name='Scott');