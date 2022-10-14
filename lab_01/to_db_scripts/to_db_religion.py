import psycopg2
from config import host, user, password, db_name
from pars_rel import getInfo

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

	f = open('religions.txt', encoding='utf-8')
	for line in f:
		data = getInfo(line[:-1])
		print(data)
		cursor.execute( """INSERT INTO "Религия" ("Название", "Тип", "Распространение", "Духовентсво") VALUES (%s, %s, %s, %s) """, (data.get('Название'), data.get('Тип'), data.get('Распространение'), data.get('Духовенство')))
	f.close()
	#cursor.execute( """INSERT INTO "Королевства" ("Название", "Река", "Местонахождение", "Население") VALUES (%s, %s, %s, %s) """, (data.get('Название'), data.get('Река'), data.get('Местонахождение'), data.get('Население')))
except Exception as _ex:
	print("[INFO] Error while working", _ex)
finally:
	if connection:
		cursor.close()
		connection.close()
		print("[INFO] Connection closed")