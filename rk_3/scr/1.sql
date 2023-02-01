create table employee (
	id int not null primary key,
	name text,
	birthdate date, 
	department text
);

create table record(
	employee_id int references employee(id) not null,
	rdate date,
	day text,
	rtime time,
	rtype int
);
insert into employee(id,name, birthdate, department)
	values
	(2, 'Глотов Илья А.', '03-09-1999', 'IT'),
	(3, 'Волгина Ольга Н.', '05-09-1990', 'Fin'),
	(4, 'Загаинов Никита С.', '05-09-1997', 'IT'),
	(5, 'Карпова Екатерина О.', '03-10-1996', 'IT'),
	(6, 'Княжев Алексей В.', '05-04-1991', 'IT'),
	(7, 'Лемешев Александр С.', '06-03-1994', 'Fin'),
	(8, 'Ляпина Наталья В.', '09-07-1994', 'IT'),
	(9, 'Морозов Дмитрий В.', '08-08-1998', 'IT'),
	(10, 'Нарандаев Дамир С.', '07-10-1996', 'Fin'),
	(11, 'Обревская Вероника И.', '04-12-1990', 'IT'),
	(12, 'Худяков Владимир С.', '08-12-1991', 'IT'),
	(13, 'Толкачев Илья В.', '03-02-1999', 'Fin'),
	(14, 'Ратников Владислав И.', '08-03-1992', 'Fin'),
	(15, 'Шацкий Никита С.', '01-09-2001', 'Fin'),
	(16, 'Кострицкий Александр С.', '01-04-1993', 'IT'),
	(17, 'Гаврилова Юлия М.', '05-05-1997', 'IT');

insert into record(employee_id, rdate, day, rtime, rtype)
	values
	(1, '12-21-2019', 'Понедельник', '09:01', 1),
	(1, '12-21-2019', 'Понедельник', '09:12', 2),
	(1, '12-21-2019', 'Понедельник', '09:40', 1),
	(1, '12-21-2019', 'Понедельник', '20:01', 2),

	(3, '12-21-2019', 'Понедельник', '09:01', 1),
	(5, '12-21-2019', 'Понедельник', '09:12', 2),
	(3, '12-21-2019', 'Понедельник', '09:40', 1),
	(5, '12-21-2019', 'Понедельник', '20:01', 2),

	(2, '12-21-2019', 'Понедельник', '08:51', 1),
	(7, '12-21-2019', 'Понедельник', '20:31', 2),

	(4, '12-21-2019', 'Понедельник', '09:51', 1),
	(6, '12-21-2019', 'Понедельник', '20:31', 2),

	(1, '12-23-2019', 'Среда', '09:11', 1),
	(8, '12-23-2019', 'Среда', '09:12', 2),
	(8, '12-23-2019', 'Среда', '09:40', 1),
	(10, '12-23-2019', 'Среда', '20:01', 2),

	(12, '12-23-2019', 'Среда', '09:01', 1),
	(3, '12-23-2019', 'Среда', '09:12', 2),
	(13, '12-23-2019', 'Среда', '09:50', 1),
	(15, '12-23-2019', 'Среда', '20:01', 2),

	(2, '12-23-2019', 'Среда', '08:41', 1),
	(16, '12-23-2019', 'Среда','20:31', 2),

	(4, '12-23-2019', 'Среда', '09:51', 1),
	(16, '12-23-2019', 'Среда', '20:31', 2);

insert into record(employee_id, rdate, day, rtime, rtype)
	values
	(8, '12-23-2019', 'Среда', '12:01', 2),
	(8, '12-23-2019', 'Среда', '11:01', 2),
	(8, '12-23-2019', 'Среда', '10:01', 2);
--Написать скалярную функцию, возвращающую количество сотрудников в возрасте от 18 до
--40, выходивших более 3х раз.
create or replace function latters_cnt(target_date date) returns int as $$
	BEGIN
		RETURN(select count(*)
		from (
			select distinct id
			from employee
			where extract(year from current_date) - extract(year from birthdate) BETWEEN 18 AND 40 and
			id in(
				select employee_id
				from(
					select employee_id, rdate, rtype, count(*)
					from record
					where rdate = target_date
					group by employee_id, rdate, rtype
					having rtype = 2 and count(*) > 3) as tmp
				)
			) as tmp2
		);
	END;
	$$ language plpgsql;
select * from latters_cnt('12-23-2019')


-- Найти все отделы, в которых есть более 10 сотрудников
select * from (select department, count(distinct id) as c
from employee e group by department) as tmp where tmp.c > 10

-- Найти сотрудников, которые не выходят с рабочего места в течении всего рабочего дня
select distinct employee_id
from record r 
where rtype = 2
group by employee_id, day
having COUNT(*) = 1; 

-- Найти все отделы, в которых есть сотрудники, опоздавшие в определенную дату.

select department, count(distinct employee_id)
from employee e
join
record r on r.employee_id = e.id
where r.rtime > '9:00' and rtype = 1 and rdate = '12-23-2019'
group by department