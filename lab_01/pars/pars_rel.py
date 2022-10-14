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
				res.update({"type":i.text})
		if (d == "Местоположение"):
			item = hui.find_all('div', class_='pi-data-value pi-font')
	
			for i in item:
				res.update({"propagation":i.text[:40]})
		if (d == "Духовенство"):
			item = hui.find_all('div', class_='pi-data-value pi-font')
	
			for i in item:
				res.update({"clergy":i.text[:40]})

	if res.get("type") == None:
		res.update({"type" : "Генотеизм"})
	if res.get("clergy") == None:
		res.update({"clergy" : "Не известно"})
	if res.get("propagation") == None:
		res.update({"propagation" : "Слишком мало"})
	res.update({"followers" : random.randint(100, 100000)})
	return res

with open('religions.csv', 'w', newline='') as file:
	writer = csv.writer(file, delimiter=';')
	writer.writerow(['Id_religion','name','type','clergy','propagation', 'followers'])
	f = open('religions.txt', encoding='utf-8')
	i = 1;
	for line in f:
		data = getInfo(line[:-1])
		writer.writerow([i, data.get('name'), data.get('type'),data.get('clergy'), data.get('propagation'), data.get('followers')])
		i+=1
	f.close()