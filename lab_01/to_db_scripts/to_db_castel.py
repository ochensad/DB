import psycopg2
from config import host, user, password, db_name
from pars_castel import getInfo

try:
	# Подключаемся к бд
	connection = psycopg2.connect(
		host = host,
		user = user,
		password = password,
		database = db_name
		)
	connection.autocommit = True
	# Создаем курсор
	cursor = connection.cursor()
	cursor.execute(
		"SELECT version();")
	print(f"Server version: {cursor.fetchone()}")

	f = open('castels.txt', encoding='utf-8')
	for line in f:
		data = getInfo(line[:-1])
		
		sql = """SELECT "id_королевства" FROM public."Королевства" WHERE "Название" = %s"""
		adr = (data.get('Местонахождение'), )
		cursor.execute(sql, adr)
		p = cursor.fetchall()
		for x in p:
			data.update({"Id_Королевства" : x[0]})

		sql = """SELECT "id_дома" FROM public."Дома" WHERE "Название" = %s"""
		adr = (data.get('Правители'), )
		cursor.execute(sql, adr)
		p = cursor.fetchall()
		for x in p:
			data.update({"Id_дома" : x[0]})

		sql = """SELECT "id_религии" FROM public."Религия" WHERE "Название" = %s"""
		adr = (data.get('Религия'), )
		cursor.execute(sql, adr)
		p = cursor.fetchall()
		for x in p:
			data.update({"Id_религии" : x[0]})
		print(data)
		cursor.execute( """INSERT INTO "Замок" ("Название", "Тип", "Население", "id_королевства", "id_дома", "id_религии") VALUES (%s, %s, %s, %s, %s, %s) """, (data.get('Название'), data.get('Тип'), data.get('Население'), data.get('Id_Королевства'), data.get('Id_дома'), data.get('Id_религии')))
	f.close()
except Exception as _ex:
	print("[INFO] Error while working", _ex)
finally:
	if connection:
		cursor.close()
		connection.close()
		print("[INFO] Connection closed")