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

	Kingdom = ['Север',
	'Западные земли',
	'Дорн',
	'Простор',
	'Долина Аррен',
	'Речные земли',
	'Штормовые земли',
	'Королевские земли',
	'Железные острова',
	'Вольные города',
	'Полуостров Валирия',
	'Залив Драконов',
	'Сарнор',
	'Дотракийское море',
	'Лхазар',
	'Красные пустоши',
	'Кварт',
	'Иббен',
	'Равнины Джогос Нхай',
	'Йи Ти',
	'Асшай',
	'Край Теней',
	'Стена',
	'Дар',
	'Земли за Стеной']

	Houses = ["Дастины", "Мандерли", "Флинты" ,"Гловеры", "Сервины" ,"Карстарки" ,"Мормонты" ,"Амберы", "Рисвеллы", "Риды", "Локи", "Толхарты", "Хорнвуды",
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
	res = {}
	for n in names:
		name = n.text[6:]
		res.update({"name":name[:-4]})

	for hui in huii:
		d = hui.get('data-source')
		if (d == "Местонахождение"):
			item = hui.find_all('div', class_='pi-data-value pi-font')
	
			for i in item:
				res.update({"Местонахождение":i.text})
		if (d == "Тип"):
			item = hui.find_all('div', class_='pi-data-value pi-font')
	
			for i in item:
				res.update({"type":i.text})
		if (d == "Правители"):
			item = hui.find_all('div', class_='pi-data-value pi-font')
	
			for i in item:
				res.update({"Правители":i.text})
		if (d == "Религия"):
			item = hui.find_all('div', class_='pi-data-value pi-font')
	
			for i in item:
				res.update({"Религия":i.text})

	res.update({"population" : random.randint(100, 1000)})
	res.update({"age" : random.randint(1000, 2000)})

	if res.get("Местонахождение") == None:
		res.update({"Местонахождение" : "Общие земли"})
	if res.get("Местонахождение") == "Север, Вестерос":
		res.update({"Местонахождение" : "Север"})
	if "Речные земли" in res.get("Местонахождение"):
		res.update({"Местонахождение" : "Речные земли"})
	if res.get("Местонахождение") == "Штормовые земли, Вестерос":
		res.update({"Местонахождение" : "Штормовые земли"})
	if res.get("Местонахождение") == "Западные земли, Вестерос":
		res.update({"Местонахождение" : "Западные земли"})
	if "Королевские земли" in res.get("Местонахождение"):
		res.update({"Местонахождение" : "Королевские земли"})
	if res.get("Местонахождение") == "Дорн, Вестерос":
		res.update({"Местонахождение" : "Дорн"})
	if "Долина Аррен" in res.get("Местонахождение"):
		res.update({"Местонахождение" : "Долина Аррен"})
	if res.get("Местонахождение") == "Простор, Вестерос":
		res.update({"Местонахождение" : "Простор"})
	if "Черноводный залив" in res.get("Местонахождение"):
		res.update({"Местонахождение" : "Королевские земли"})
	if "Узкое море" in res.get("Местонахождение"):
		res.update({"Местонахождение" : "Королевские земли"})
	if "Вестерос" in res.get("Местонахождение"):
		res.update({"Местонахождение" : "Королевские земли"})
	if "Железные острова" in res.get("Местонахождение"):
		res.update({"Местонахождение" : "Железные острова"})

	if res.get("type") == None:
		res.update({"type" : "Замок"})
	if res.get("Религия") == None and res.get("Местонахождение") == 'Север':
		res.update({"Религия" : "Старые Боги"})
	if res.get("Религия") == None:
		res.update({"Религия" : "Вера в Семерых"})
	if "(ранее)" in res.get("Религия"):
		res.update({"Религия" : res.get("Религия")[:-8]})
	if "Старые Боги" in res.get("Религия"):
		res.update({"Религия" : "Старые Боги"})
	if "Утонув" in res.get("Религия"):
		res.update({"Религия" : "Утонувший Бог"})
	if res.get("Правители") == None and res.get("Местонахождение") == 'Север':
		res.update({"Правители" : "Старки"})
	if res.get("Правители") == None and res.get("Местонахождение") == 'Королевские земли':
		res.update({"Правители" : "Баратеоны"})
	if res.get("Правители") == None and res.get("Местонахождение") == 'Дорн':
		res.update({"Правители" : "Мартеллы"})
	if res.get("name") == 'Хайгарден':
		res.update({"Правители" : "Тиреллы"})
	if res.get("Правители") == None and res.get("Местонахождение") == 'Простор':
		res.update({"Правители" : "Тиреллы"})
	if res.get("Правители") == None and res.get("Местонахождение") == 'Штормовые земли':
		res.update({"Правители" : "Баратеоны"})
	if res.get("Правители") == None and res.get("Местонахождение") == 'Долина Аррен':
		res.update({"Правители" : "Аррены"})
	if res.get("Правители") == None and res.get("Местонахождение") == 'Западные земли':
		res.update({"Правители" : "Ланнистеры"})
	if res.get("Правители") == None and res.get("Местонахождение") == 'Железные острова':
		res.update({"Правители" : "Грейджои"})
	if res.get("Правители") == None and res.get("Местонахождение") == 'Речные земли':
		res.update({"Правители" : "Талли"})
	if "(ранее)" in res.get("Правители"):
		res.update({"Правители" : res.get("Правители")[:-8]})
	k = res.get("Правители").rfind(')')
	if k != -1:
		res.update({"Правители" : res.get("Правители")[k+1:]})
	if "Флинты" in res.get("Правители"):
		res.update({"Правители" : "Флинты"})
	if "Баратеоны" in res.get("Правители"):
		res.update({"Правители" : "Баратеоны"})
	if "Морригены" in res.get("Правители"):
		res.update({"Правители" : "Морригены"})
	if res.get("Правители") == 'Король Андалов и Первых Людей':
		res.update({"Правители" : "Старки"})
	if res.get("Правители") == 'Росби':
		res.update({"Правители" : "Росби (дом)"})
	try:
		ind = Kingdom.index(res.get('Местонахождение'))
	except ValueError:
		ind = random.randint(0, len(Kingdom))
	res.update({"id_k": ind + 1})
	try:
		ind = Houses.index(res.get('Правители'))
	except ValueError:
		ind = random.randint(0, len(Houses))
	res.update({"id_h": ind + 1})
	try:
		ind = Relig.index(res.get('Религия'))
	except ValueError:
		ind = random.randint(0, len(Relig))
	res.update({"id_r": ind + 1})
	return res

def getName():
	name_1 = ["Дубовый", "Кленовый", "Каменный", "Солнечный", "Ветренный", "Высокий", "Зимний", "Старый", "Золотой", "Красный", "Белый", "Теплый", "Холодный", "Одинокий",
				"Летний", "Дальний", "Морской", "Солёный", "Черный", "Тихий", "Желтый", "Железный", "Стальной", "Снежный", "Песчаный", "Лунный", "Цветочный", "Забытый",
				"Отчий", "Облачный", "Драконий", "Небесный", "Звездный", "Розовый"]
	name_2 = ["Брод", "Пруд", "Причал", "Холм", "Зуб", "Лес", "Город", "Приют", "Холл", "Дом", "Замок", "Очаг", "Предел", "Чертог", "Венец", "Дуб", "Мост", "Берег", "Сад",
				"Дол", "Камень", "Удел", "Дозор", "Утес", "Залив"]
	res = name_1[random.randint(0, len(name_1) - 1)] + " " + name_2[random.randint(0, len(name_2) - 1)]
	return res
def getType():
	type_1 = ["Замок", "Башня", "Крепость", "Город", "Поселение"]
	return type_1[random.randint(0, len(type_1) - 1)]

def getPopulation():
	return random.randint(100, 1000)

def getAge():
	return random.randint(1000, 2000)

def getIdh():
	return random.randint(1, 1002)

def getIdr():
	return random.randint(1, 14)

def getIdk():
	return random.randint(1, 24)

with open('castels.csv', 'w', newline='') as file:
	writer = csv.writer(file, delimiter=';')
	f = open('castels.txt', encoding='utf-8')
	i = 1;
	for line in f:
		print(i)
		data = getInfo(line[:-1])
		writer.writerow([i, data.get('name'), data.get('type'),data.get('population'), data.get('age'), data.get('id_h'), data.get('id_r'), data.get('id_k')])
		i+=1
	f.close()
	for j in range(0, 872):
		print(j)
		writer.writerow([i, getName(), getType() , getPopulation() , getAge() , getIdh() ,getIdr(), getIdk()])
		i+=1
