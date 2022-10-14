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

	res = {}
	for n in names:
		name = n.text[6:]
		res.update({"name":name[:-4]})

	for hui in huii:
		d = hui.get('data-source')
		if (d == "Тип"):
			item = hui.find_all('div', class_='pi-data-value pi-font')
	
			for i in item:
				res.update({"type":i.text[:40]})
		if (d == "Местонахождение"):
			item = hui.find_all('div', class_='pi-data-value pi-font')
	
			for i in item:
				res.update({"location":i.text[:40]})
		if (d == "Статус"):
			item = hui.find_all('div', class_='pi-data-value pi-font')
	
			for i in item:
				res.update({"state":i.text[:40]})

	if res.get("type") == None:
		res.update({"type" : "Отряд"})
	if res.get("location") == None:
		res.update({"location" : "Не известно"})
	if res.get("state") == None:
		res.update({"state" : "Активный"})
	res.update({"followers" : random.randint(10, 500)})
	return res

with open('organizations.csv', 'w', newline='') as file:
	writer = csv.writer(file, delimiter=';')
	f = open('organizations.txt', encoding='utf-8')
	i = 1;
	writer.writerow(['id', 'name', 'type','location','state','followers'])
	for line in f:
		print(i)
		data = getInfo(line[:-1])

		writer.writerow([i, data.get('name'), data.get('type'),data.get('location'), data.get('state'), data.get('followers')])
		i+=1
	f.close()
