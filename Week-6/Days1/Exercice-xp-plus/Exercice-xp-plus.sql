create table étudiants(
	etudiant_id serial primary key,
	last_name varchar(50) not null,
	first_name varchar(50) not null,
	birth_date Date not null
);

insert into étudiants(last_name,first_name,birth_date)
values('Marc','Bénichou','02/11/1998'),
		('Yann','Cohen','03/12/2010'),
		('Léa','Bénichou','27/07/1987'),
		('Amélia','Dux','07/04/1996'),
		('David	','Grez','14/06/2003'),
		('Omer','Simpson','03/10/1980'),
		('Ibrahim','Neya','06/12/1999');
insert into étudiants(last_name,first_name,birth_date)
values('Léah','Bénichou','27/07/1987');

select *from étudiants
select last_name,first_name from étudiants
select last_name,first_name from étudiants where etudiant_id=2
select last_name,first_name from étudiants where last_name='Marc' and first_name='Bénichou'
select last_name,first_name from étudiants where last_name='Marc' or first_name='Bénichou'
select last_name,first_name from étudiants where last_name like '%a%'
select last_name,first_name from étudiants where last_name like 'a%'
select last_name,first_name from étudiants where last_name like '%a'
select last_name,first_name from étudiants where last_name like '%a_'
select last_name,first_name from étudiants where etudiant_id=1 and etudiant_id=3
select last_name,first_name from étudiants where birth_date<='01/01/2000'

