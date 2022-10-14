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
	all_rivers = vse.find_all('div' , class_ = 'pi-item pi-data pi-item-spacing pi-border-color')

	river_arr = []
	i = 0
	i_needed = -1
	for cur_rivers in all_rivers:
		cur = cur_rivers.find_all('h3' , class_ = 'pi-data-label pi-secondary-font')
		for name in cur:
			if name.text == "Реки и заливы":
				i_needed = i
				break
			if name.text == "Реки и озера":
				i_needed = i
				break
			if name.text == "Реки":
				i_needed = i
				break
		i += 1
		if (i_needed != -1):
			break

	river = ""
	if (i_needed != -1):
		tmp_river = all_rivers[i_needed].find_all('div', class_ = 'pi-data-value pi-font')
		for cur_tmp_river in tmp_river:
			names_r = cur_tmp_river.find_all('a')
			for name_r in names_r:
				river_arr.append(name_r.text)

		river = river_arr[random.randint(0, (len(river_arr) - 1))]
	res = {}
	for n in names:
		name = n.text[6:]
		res.update({"name":name[:-4]})

	for hui in huii:
		d = hui.get('data-source')
		if (d == "Местонахождение"):
			item = hui.find_all('div', class_='pi-data-value pi-font')
	
			for i in item:
				res.update({"location":i.text})

	res.update({"population" : random.randint(10000, 100000)})
	if river == "":
		river = "Не указана"
	res.update({"main_river" : river})
	if res.get("location") == None:
		res.update({"location" : "Общие земли"})
	res.update({"exist" : random.randint(0, 1)})
	if (res.get('exist') == 0):
		res.update({'exist' : False})
	else:
		res.update({'exist' : True})
	return res

with open('kindoms.csv', 'w', newline='') as file:
	writer = csv.writer(file, delimiter=';')

	f = open('kindoms.txt', encoding='utf-8')
	i = 1;
	for line in f:
		data = getInfo(line[:-1])
		writer.writerow([i, data.get('name'), data.get('main_river'),data.get('location'), data.get('population'), data.get('exist')])
		i+=1
	f.close()