from bs4 import BeautifulSoup
import requests
import random
import csv

def getInfo(site):

	url = site
	response = requests.get(url)
	vse = BeautifulSoup(response.text, 'lxml')
	huii = vse.find_all('div', class_='pi-item pi-data pi-item-spacing pi-border-color')
	names = vse.find_all('h1', class_='page-header__title')

	Houses = ["Старки","Болтоны","Дастины", "Мандерли", "Флинты" ,"Гловеры", "Сервины" ,"Карстарки" ,"Мормонты" ,"Амберы", "Рисвеллы", "Риды", "Локи", "Толхарты", "Хорнвуды",
			"Пули", "Гринлифы", "Кассели", "Мейзины" ,"Моллены", "Форрестеры" ,"Дормунды", "Гленморы", "Уэллсы", "Марши", "Уайтхиллы", "Холты", "Браунбэрроу", 
			"Грейсоны","Тауэрсы", "Элливеры","Эмберы","Фросты","Талли","Блэквуды","Бракены","Маллистеры","Мутоны","Смоллвуды","Фреи","Уоды","Хеддли","Хэи","Эренфорды", 
			"Бейлиши","Дарри" ,"Джастмены","Квохерисы","Лотстоны","Мадды","Стронги","Уэнты","Харровеи","Аррены","Белморы","Игены","Корбреи","Линдерли","Ройсы",
			"Толлетты","Уэйнвуды","Хантеры","Муры","Ланнистеры","Вестерлинги","Крейкхоллы","Ланнистеры из Ланниспорта","Леффорды","Марбранды","Пейны","Сарсфилды",
			"Серретты","Ярвики","Гринфилды","Лорхи","Свифты","Хезерспуны","Кастерли","Клиганы","Рейны","Тарбеки","Блаунты","Брюны","Гонты","Кеттлблэки","Риккеры",
			"Росби (дом)","Слинты","Стокворты","Стонтоны","Торны","Челстеды","Бар-Эммоны","Веларионы","Селтигары","Таргариены","Блэкфайры","Дарклины","Каргиллы",
			"Холларды","Баратеоны из Королевской Гавани","Баратеоны из Драконьего Камня"",Баратеоны,Баклеры","Грандисоны","Масгуды","Морригены","Пенрозы","Пизбери",
			"Тарты","Трэнты","Уайлды","Эрролы","Эстермонты","Дондаррионы","Кароны","Сванны","Селми","Коннингтоны","Сиворты","Дюррандоны","Коли","Тойны","Дом Бронна",
			"Тиреллы","Гарденеры","Бисбери","Бранфилды","Булверы","Вебберы","Дурвеллы","Инчфилды","Костейны","Кью","Лейгуды","Маллендоры","Мерривезеры","Окхарты",
			"Осгреи","Редвины","Рованы","Стрикленды","Тарли","Флоренты","Фоссовеи","Хайтауэры","Хаствики","Эшфорды","Мартеллы","Айронвуды","Аллирионы","Блэкмонты",
			"Гаргалены","Дальты","Дейн","Джордейны","Драйленды","Кворгилы","Манвуди","Сантагары","Уллеры","Фаулеры","Грейджои","Хоары","Блектайды","Ботли","Гудбрайзеры",
			"Драммы","Кеннинги","Мерлины","Хамблы","Харлоу","Блекброу","Колфилды","Ранкенфеллы","Уибберли"]
	Relig = ["Вера в Семерых", "Старые Боги" ,"Утонувший Бог" ,"Многоликий" ,"Владыка Света" ,"Великий Жеребец", "Великий Иной", "Лев Ночи" ,"Дева-из-Света","Великий Пастух",
			"Плачущая Госпожа", "Бородатые жрецы", "Чёрный Козёл", "Лунные Певицы"]
	sex = ["ж", "м"]
	st = [True, False]
	res = {}
	for n in names:
		name = n.text[6:]
		res.update({"Имя":name[:-4]})

	for hui in huii:
		d = hui.get('data-source')
		if (d == "Родина"):
			item = hui.find_all('div', class_='pi-data-value pi-font')
	
			for i in item:
				res.update({"Родина":i.text[:100]})
		if (d == "Титул"):
			item = hui.find_all('div', class_='pi-data-value pi-font')
	
			for i in item:
				res.update({"Титул":i.text[:40]})
		if (d == "Культура"):
			item = hui.find_all('div', class_='pi-data-value pi-font')
	
			for i in item:
				res.update({"Культура":i.text[:40]})
		if (d == "Религия"):
			item = hui.find_all('div', class_='pi-data-value pi-font')
	
			for i in item:
				res.update({"Религия":i.text})

	if res.get("Титул") == None:
		res.update({"Титул" : "Нет"})
	if res.get("Родина") == None:
		res.update({"Родина":"Неизвестно"})
	if res.get("Культура") == None:
		res.update({"Культура":"Неизвестно"})
	if res.get("Религия") == None:
		res.update({"Религия": random.randint(1,len(Relig))})
	else:
		try:
			ind = Relig.index(res.get('Религия'))
		except ValueError:
			ind = random.randint(0, len(Relig) - 1)
		res.update({"Религия": ind + 1})

	k = res.get("Имя").rfind(' ')
	if (res.get("Имя")[k+1:] == "Сэнд"):
		res.update({"Дом":145})
	if (res.get("Имя")[k+1:] == "Сноу"):
		res.update({"Дом":1})

	for l in Houses:
		if res.get("Имя")[k +1:-1] in l:
			res.update({"Дом": Houses.index(l) + 1})
	if res.get("Дом") == None:
		res.update({"Дом": random.randint(176,1000)})

	res.update({"Пол" : sex[random.randint(0,1)]})
	res.update({"Возраст" : random.randint(10,80)})
	res.update({"Жив" : st[random.randint(0,1)]})
	return res

def getName():
	name_1 = ["Джон", "Родрик", "Титос", "Лианна", "Джейн", "Айрис", "Амелия", "Глория", "Иви", "Камила",
	"Леона", "Марша","Пеги","Одри","Сандра","Тина","Флоранс","Шерри","Элеонора","Рут","Адриан","Эндрю",
	"Остин","Бернард","Кэйлеб","Клейтон","Даглас","Изекил","Грант","Джером","Луис","Лестер","Мартин","Нэйтен",
	"Шейн","Теренс","Уолтер","Стивен","Мэтью","Кит","Джек"]
	name_2 = []
	oi = open('house_names.txt', encoding='utf-8')
	for line in oi:
		name_2.append(line[:-1])
	oi.close()
	res = name_1[random.randint(0, len(name_1) - 1)] + " " + name_2[random.randint(0, len(name_2) - 1)]
	return res
def getSex():
	type_1 = ["ж", "м"]
	return type_1[random.randint(0, len(type_1) - 1)]

def getCulture():
	type_1 = ["Андалы", "Северяне", "Райнары","Валирийцы", "Вольный народ", "Дотракийцы"]
	return type_1[random.randint(0, len(type_1) - 1)]

def getTitle():
	type_1 = ["Лорд", "Сир", "Магистр", "Септон"]
	return type_1[random.randint(0, len(type_1) - 1)]

def getMotherland():
	type_1 = ["Вестерос", "Эссос"]
	return type_1[random.randint(0, len(type_1) - 1)]

def getAge():
	return random.randint(1, 80)

def getIdh():
	return random.randint(176, 1002)

def getIdr():
	return random.randint(1, 14)

def getState():
	type_1 = [True, False]
	return type_1[random.randint(0, len(type_1) - 1)]

with open('persons.csv', 'w', newline='') as file:
	writer = csv.writer(file, delimiter=';')
	writer.writerow(['id_character','name', 'sex','culture', 'title', 'motherland', 'age', 'alive' , 'id_religion', 'id_house'])
	f = open('persons.txt', encoding='utf-8')
	i = 1;
	for line in f:
		print(i)
		data = getInfo(line[:-1])
		writer.writerow([i, data.get('Имя'), data.get('Пол'),data.get('Культура'), data.get('Титул'), data.get('Родина'), data.get('Возраст'), data.get('Жив'), data.get("Религия"), data.get("Дом")])
		i+=1
	f.close()
	for j in range(0, 872):
		print(j)
		writer.writerow([i, getName(), getSex() , getCulture() , getTitle(), getMotherland(), getAge() , getState() ,getIdr(), getIdh()])
		i+=1