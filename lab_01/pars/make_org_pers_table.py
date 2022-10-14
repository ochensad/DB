import csv
import random

def getIdo():
	return random.randint(1, 36)

def getIdc():
	return random.randint(1, 1002)

def getState():
	type_1 = [True, False]
	return type_1[random.randint(0, len(type_1) - 1)]

def getYearsIn():
	return random.randint(1, 50)

def checkIn(arr, a):
	for i in range(0, len(arr)):
		if arr[i][0] == a[0] and arr[i][1] == a[1]:
			return False;
	return True;

data = []
data_i = [] 

with open('organizations_and_persons.csv', 'w', newline='') as file:
	writer = csv.writer(file, delimiter=';')
	writer.writerow(['Id_organization', 'Id_character', 'state', 'years_in'])
	for j in range(0, 1000):
		print(j)
		data_i = [getIdo(), getIdc() , getState() , getYearsIn()]
		while checkIn(data, data_i) == False:
			data_i = [getIdo(), getIdc() , getState() , getYearsIn()]
		data.append(data_i)
		writer.writerow(data_i)