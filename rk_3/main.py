from peewee import *
from datetime import *

FirstQ = """
SELECT * from (select department, count(distinct id) as c
from employee e group by department) as tmp where tmp.c > 10;
"""

SecondQ = """
SELECT distinct employee_id
from record r 
where rtype = 2
group by employee_id, day
having COUNT(*) = 1;
"""

# Создаем соединение с базой данных
con = PostgresqlDatabase(
    database='postgres',
    user='postgres',
    password='1234',
    host='localhost', 
    port="5432"
)

class BaseModel(Model):
    class Meta:
        database = con


class Employee(BaseModel):
    id = IntegerField(column_name='id')
    name = CharField(column_name='name')
    birthdate = DateField(column_name='birthdate')
    department = CharField(column_name='department')

    class Meta:
        table_name = 'employee'

class Record(BaseModel):
    employee_id = ForeignKeyField(Employee, backref='employee_id')
    rdate = DateField(column_name='rdate')
    day =  CharField(column_name='day')
    rtime = TimeField(column_name='rtime')
    rtype = IntegerField(column_name='rtype')	

    class Meta:
        table_name = 'record'

def check_date(str):
    i = 0
    day = ''
    mounth = ''
    year = ''
    for k in str:
        if k == '-':
            i+=1
        else:
            if i == 0:
                mounth += k
            elif i == 1:
                day +=k
            elif i == 2:
                year += k
    if (int(mounth) > 12):
        return False
    if (int(day) > 31):
        return False
    return True
def Task1():
    global con

    cur = con.cursor()

    cur.execute(FirstQ)
    print("Запрос 1:\n")
    rows = cur.fetchall()
    for row in rows:
        print(*row)

    cur.execute(SecondQ)
    print("\nЗапрос 2:\n")
    rows = cur.fetchall()
    for row in rows:
        print(*row)


    date = input("Введите дату: ")
    while check_date(date) != True:
        date = input("Введите дату")

    cur.execute("""SELECT department, count(distinct employee_id)
from employee e
join
record r on r.employee_id = e.id
where r.rtime > '9:00' and rtype = 1 and rdate = '""" + date + """' group by department;""")
    print("\nЗапрос 3:\n")
    rows = cur.fetchall()
    for row in rows:
        print(*row)

    cur.close()

def Task2():
    global con

    cur = con.cursor()

    print("2. Найти сотрудников, которые не выходят с рабочего места в течении всего рабочего дня")
    query = Record.select((Record.employee_id)).where(Record.rtype == 2).group_by(Record.employee_id, Record.day).having(fn.Count(Record.employee_id) == 1)
    for q in query.dicts().execute():
        print(q)
        
    print("3. Найти все отделы, в которых есть сотрудники, опоздавшие в определенную дату.")
    date = input("Введите дату: ")
    while check_date(date) != True:
        date = input("Введите дату")
    query = Employee.select(Employee.department, fn.Count(Employee.employee_id)).join(Record).where(Record.rtime > '09:00:00').where(Record.rtype==1).where(Record.rdate == date).group_by(Employee.department)
    for q in query.dicts().execute():
        print(q)

    cur.close()
	

def main():
	Task1()
	Task2()

	con.close()

if __name__ == "__main__":
	main()