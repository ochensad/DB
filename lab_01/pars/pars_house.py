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

	state = [True, False]
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
	res = {}
	for n in names:
		name = n.text[6:]
		res.update({"name":name[:-4]})

	for hui in huii:
		d = hui.get('data-source')
		p = hui.find_all('h3', class_ = 'pi-data-label pi-secondary-font')
		for l in p:
			if (l.text == "Герб"):
				item = hui.find_all('div', class_='pi-data-value pi-font')
	
				for i in item:
					res.update({"blazon":i.text[:40]})
		if (d == "Девиз"):
			item = hui.find_all('div', class_='pi-data-value pi-font')
	
			for i in item:
				res.update({"motto":i.text[:40]})
		if (d == "Область"):
			item = hui.find_all('div', class_='pi-data-value pi-font')
	
			for i in item:
				res.update({"Область":i.text})

	if res.get("Область") == None:
		res.update({"Область" : "Асшай"})
	if res.get("Область") == 'Север, Весторос':
		res.update({"Область" : "Север"})
	if res.get("Область") == "Север ":
		res.update({"Область" : "Север"})
	if res.get("Область") == "Речные землиДолина Аррен":
		res.update({"Область" : "Речные земли"})
	if res.get("Область") == "Железные острова Речные земли":
		res.update({"Область" : "Железные острова"})
	if res.get("blazon") == None:
		res.update({"blazon" : "Не известен"})
	if res.get("motto") == None:
		res.update({"motto" : "Не известен"})
	if res.get("name") == 'Таргариены':
		res.update({"Область" : "Королевские земли"})
	if res.get("name") == 'Вольный народ':
		res.update({"Область" : "Земли за Стеной"})
	res.update({"followers" : random.randint(10, 1000)})
	res.update({"exist" : state[random.randint(0, 1)]})
	try:
		ind = Kingdom.index(res.get('Область'))
	except ValueError:
		ind = random.randint(0, len(Kingdom))
	res.update({"id_k": ind + 1})
	return res

def getName():
	name_1 = ["Вуд", "Хоа", "Гиб", "Блэк", "Рив", "Бра", "Стоун", "Веб", "Сан", "Кра", "Брид", "Фиц"]
	name_2 = ["пер", "ки", "бер", "дра", "тиг", "кев", "дур", "выс", "шет", "лив", "ном", "лер", "цак", ""]
	name_3 = ["ры", "лоу", "ммы", "ли", "ки", "ты", "веи", "ды", "ны", "ри", "оны", "хи"]
	res = name_1[random.randint(0, len(name_1) - 1)] + name_2[random.randint(0, len(name_2) - 1)] + name_3[random.randint(0, len(name_3) - 1)]
	return res

def getBlazon():
	blazon_1 = ["Лев", "Бык", "Конь", "Собака", "Кошка", "Овца", "Волк", "Медведь", "Лань", "Олень", "Кабан", "Слон", "Антилопа", "Кролик",
	"Орёл", "Павлин", "Пеликан", "Ворон", "Журавль", "Сокол", "Лебедь", "Сова", "Страус","Аист", "Грач", "Попугай", "Утка", "Ласточка","Пчела",
	"Муравей", "Бабочка", "Дельфин", "Морская раковина", "Змей", "Дуб", "Оливковое дерево", "Пальма"]
	blazon_2 = ["Абрикосовом", "Аквамариновом",
	"Ализариновый красном",
	"Алом",
	"Амарантово-пурпурном",
	"Амарантово-розовом",
	"Амарантовом",
	"Амарантовый глубоко-пурпурном",
	"Амарантовый светло-вишневом",
	"Аметистовом",
	"Аспидно-сером",
	"Аспидно-синем",
	"Базальтово-сером",
	"Бежево-коричневом",
	"Бежево-красном",
	"Бежево-сером",
	"Бежевом",
	"Бело-алюминиевом",
	"Бело-зеленом",
	"Белоснежном",
	"Белом",
	"Бирюзово-зеленом",
	"Бирюзово-синем",
	"Бирюзовом",
	"Бледно-васильковом",
	"Бледно-желтом",
	"Бледно-зелено-сером",
	"Бледно-зеленом",
	"Бледно-золотистом",
	"Бледно-карминном",
	"Бледно-каштановом",
	"Бледно-коричневом",
	"Бледно-песочном",
	"Бледно-пурпурном",
	"Бледно-розоватом",
	"Бледно-розовом",
	"Бледно-синем",
	"Бледно-фиолетовом",
	"Бледный желто-зеленом",
	"Бледный желто-розовом",
	"Бледный зеленовато-желтом",
	"Бледный зеленом",
	"Бледный красно-пурпурном",
	"Бледный пурпурно-розовом",
	"Бледный пурпурно-синем",
	"Бледный серо-коричневом",
	"Бледный синем",
	"Бледный фиолетово-красном",
	"Болотном",
	"Бордово-фиолетовом",
	"Бордовом",
	"Бриллиантово-синем",
	"Бронзовом",
	"Ванильном",
	"Васильковом",
	"Вересково-фиолетовом"]
	res = blazon_1[random.randint(0, len(blazon_1) - 1)] +" на " + blazon_2[random.randint(0, len(blazon_2) - 1)] + " фоне"
	return res

def getMotto():
	motto_1 = ["Мы", "Слава", "Честь", "Долг" , "Бог", "Страх", "Громкие", "Тихие", "Жизнь", "Дорога", "Защита", "Справедливость"]
	motto_2 = ["не" , "есть", "живет", ""]
	motto_3 = ["Лев", "Бык", "Конь", "Собака", "Кошка", "Овца", "Волк", "Медведь", "Лань", "Олень", "Кабан", "Слон", "Антилопа", "Кролик",
	"Орёл", "Павлин", "Пеликан", "Ворон", "Журавль", "Сокол", "Лебедь", "Сова", "Страус","Аист", "Грач", "Попугай", "Утка", "Ласточка","Пчела",
	"Муравей", "Бабочка", "Дельфин", "Морская раковина", "Змей", "Дуб", "Оливковое дерево", "Пальма"]
	res = motto_1[random.randint(0, len(motto_1) - 1)] + " " + motto_2[random.randint(0, len(motto_2) - 1)] + " " + motto_3[random.randint(0, len(motto_3) - 1)]
	return res
def getFollowers():
	return random.randint(10, 1000)

def getExist():
	state = [True, False]
	return state[random.randint(0, 1)]
def getId():
	return random.randint(1, 25)
with open('houses.csv', 'w', newline='') as file:
	writer = csv.writer(file, delimiter=';')
	f = open('houses.txt', encoding='utf-8')
	i = 1;
	for line in f:
		print(i)
		data = getInfo(line[:-1])
		writer.writerow([i, data.get('name'), data.get('blazon'),data.get('motto'), data.get('followers'), data.get('exist'), data.get('id_k')])
		i+=1
	f.close()
	for j in range(0, 826):
		print(j)
		writer.writerow([i, getName(), getBlazon() , getMotto() , getFollowers() , getExist() ,getId()])
		i+=1
