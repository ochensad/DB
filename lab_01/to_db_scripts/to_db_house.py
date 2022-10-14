import psycopg2
from config import host, user, password, db_name
from pars_house import getInfo

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

	f = open('houses.txt', encoding='utf-8')
	for line in f:
		data = getInfo(line[:-1])
		
		sql = """SELECT "id_королевства" FROM public."Королевства" WHERE "Название" = %s"""
		adr = (data.get('Область'), )
		cursor.execute(sql, adr)
		p = cursor.fetchall()
		for x in p:
			data.update({"Id_Королевства" : x[0]})
		cursor.execute( """INSERT INTO "Дома" ("Название", "Герб", "Девиз", "id_королевства") VALUES (%s, %s, %s, %s) """, (data.get('Название'), data.get('Герб'), data.get('Девиз'), data.get('Id_Королевства')))
	f.close()
except Exception as _ex:
	print("[INFO] Error while working", _ex)
finally:
	if connection:
		cursor.close()
		connection.close()
		print("[INFO] Connection closed")