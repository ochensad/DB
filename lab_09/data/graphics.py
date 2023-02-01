import matplotlib.pyplot as plt
import numpy as np

f = open('data_DbDelete.txt', 'r')
A = []
B = []

for line in f:
	k = line.find(" ")
	A.append(int(line[0: k]))
	B.append(float(line[k:]))
f.close()
x1= A
y1 = B

f = open('data_DbInsert.txt', 'r')
A = []
B = []

for line in f:
	k = line.find(" ")
	A.append(int(line[0: k]))
	B.append(float(line[k:]))
f.close()
x2= A
y2 = B

f = open('data_DbSelect.txt', 'r')
A = []
B = []

for line in f:
	k = line.find(" ")
	A.append(int(line[0: k]))
	B.append(float(line[k:]))
f.close()
x3= A
y3 = B

f = open('data_DbUpdate.txt', 'r')
A = []
B = []

for line in f:
	k = line.find(" ")
	A.append(int(line[0: k]))
	B.append(float(line[k:]))
f.close()
x4= A
y4 = B

f = open('data_RedisDelete.txt', 'r')
A = []
B = []

for line in f:
	k = line.find(" ")
	A.append(int(line[0: k]))
	B.append(float(line[k:]))
f.close()
print(A)
x5= A
y5 = B

f = open('data_RedisInsert.txt', 'r')
A = []
B = []

for line in f:
	k = line.find(" ")
	A.append(int(line[0: k]))
	B.append(float(line[k:]))
f.close()
print(A)
x6= A
y6 = B

f = open('data_RedisSelect.txt', 'r')
A = []
B = []

for line in f:
	k = line.find(" ")
	A.append(int(line[0: k]))
	B.append(float(line[k:]))
f.close()
print(A)
x7= A
y7 = B

f = open('data_RedisUpdate.txt', 'r')
A = []
B = []

for line in f:
	k = line.find(" ")
	A.append(int(line[0: k]))
	B.append(float(line[k:]))
f.close()
print(A)
x8= A
y8 = B

plt.plot(x1, y1, label = "DBDelete")
plt.plot(x5, y5, label = "RedisDelete")
plt.scatter(x1, y1, color='blue', s=20)
plt.scatter(x5, y5, color='orange', s=20)
plt.grid(True)
plt.title('')
plt.legend()
plt.ylabel('Время (мс)')
plt.xlabel('Действие')
plt.savefig('graph_1.png')
plt.show()

plt.plot(x2, y2, label = "DBInsert")
plt.plot(x6, y6, label = "RedisInsert")
plt.scatter(x2, y2, color='blue', s=20)
plt.scatter(x6, y6, color='orange', s=20)
plt.grid(True)
plt.title('')
plt.legend()
plt.ylabel('Время (мс)')
plt.xlabel('Действие')
plt.savefig('graph_2.png')
plt.show()

plt.plot(x3, y3, label = "DBSelect")
plt.plot(x7, y7, label = "RedisSelect")
plt.scatter(x3, y3, color='blue', s=20)
plt.scatter(x7, y7, color='orange', s=20)
plt.grid(True)
plt.title('')
plt.legend()
plt.ylabel('Время (мс)')
plt.xlabel('Действие')
plt.savefig('graph_3.png')
plt.show()

plt.plot(x4, y4, label = "DBUpdate")
plt.plot(x8, y8, label = "RedisUpdate")
plt.scatter(x4, y4, color='blue', s=20)
plt.scatter(x8, y8, color='orange', s=20)
plt.grid(True)
plt.title('')

plt.legend()
plt.ylabel('Время (мс)')
plt.xlabel('Действие')
plt.savefig('graph_4.png')
plt.show()
