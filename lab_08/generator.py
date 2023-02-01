import random 
import datetime
import time
import json

class character():
	# Структура полностью соответствует таблице device.
	id = int()
	name = str()
	sex = str()
	culture = str()
	title = str()
	motherland = str()
	age = int()
	alive = bool()
	id_r = int()
	id_h = int()

	def __init__(self, id, name, sex, culture, title, motherland, age, alive, id_r, id_h):
		self.id = id
		self.name = name
		self.sex = sex
		self.culture = culture
		self.title = title
		self.motherland = motherland
		self.age = age
		self.alive = alive
		self.id_r = id_r
		self.id_h = id_h

	def get(self):
		return {'Id_character': self.id, 'name': self.name, 'sex': self.sex,
				'culture': self.culture, 'title': self.title, 'motherland': self.motherland,
				'age': self.age, 'alive': self.alive, 'Id_religion': self.id_r, 'Id_house': self.id_h}

	def __str__(self):
		return f"{self.id:<2} {self.company:<20} {self.year_of_issue:<5} {self.color:<5} {self.price:<15}"

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


def main():
	color = ["blue", "red", "purple", "yellow",
			"pink", "green", "black", "white", "coral", "gold", "silver"]
	i = 1471
	j = 0


	while True:
		obj = character(j, getName(), getSex() , getCulture() , getTitle(), getMotherland(), getAge() , getState() ,getIdr(), getIdh())
		
		# print(obj)
		# print(json.dumps(obj.get()))
		
		file_name = "data/character_" + str(i) + "_" + \
			str(datetime.datetime.now().strftime("%d-%m-%Y_%H:%M:%S")) + ".json"

		print(file_name)
		
		with open(file_name, "w") as f:
			print(json.dumps(obj.get()), file=f)

		i += 1
		j += 1
		time.sleep(10)


if __name__ == "__main__":
	main()