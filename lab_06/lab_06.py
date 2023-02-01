from PyQt6 import QtCore, QtGui, QtWidgets, uic
from PyQt6.QtWidgets import QTableWidgetItem
from PyQt6.QtWidgets import QPushButton, QColorDialog
from PyQt6.QtCore import Qt
import psycopg2 as db

flag = True

class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole:
            # See below for the nested-list data structure.
            # .row() indexes into the outer list,
            # .column() indexes into the sub-list
            return self._data[index.row()][index.column()]

    def rowCount(self, index):
        # The length of the outer list.
        return len(self._data)

    def columnCount(self, index):
        # The following takes the first sub-list, and returns
        # the length (only works if all rows are an equal length)
        return len(self._data[0])

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        uic.loadUi("window.ui", self)

        self.setFixedSize(250,self.geometry().height())
        
        self.table = QtWidgets.QTableView()
        data = [
          [4, 9, 2],
          [1, 0, 0],
          [3, 5, 0],
          [3, 3, 2],
          [7, 8, 9],
        ]

        self.model = TableModel(data)
        self.table.setModel(self.model)
        self.table.show()
        self.table.setFixedSize(500, 500)
        self.scalar.clicked.connect(lambda: scalar_f(self))
        self.join.clicked.connect(lambda: join_f(self))
        self.otv.clicked.connect(lambda: otv_f(self))
        self.meta.clicked.connect(lambda: meta_f(self))
        self.scalar_func.clicked.connect(lambda: scalar_func_f(self))
        self.table_func.clicked.connect(lambda: table_func_f(self))
        self.data_proc.clicked.connect(lambda: proc_f(self))
        self.sys_func.clicked.connect(lambda: sys_f(self))
        self.create_table.clicked.connect(lambda: create_f(self))
        self.insert_to.clicked.connect(lambda: insert_f(self))
        self.flag_scalar_func = True
        self.flag_table_func = True
        self.flag_proc = True

def scalar_f(win):
    id_c = win.spinBox_scalar.value()
    query = "SELECT AVG(population) AS AVG_POPYLATION FROM Castle WHERE id_kingdom = "+ str(id_c) + " ;"
    cur.execute(query)
    result = cur.fetchone()
    data = [["Среднее население в замках"],[float(result[0])]]
    win.model = TableModel(data)
    win.table.setModel(win.model)
    win.table.setColumnWidth(0, 220)
    win.table.show()

def join_f(win):
    id_c = win.spinBox_join.value()
    query = "select T1.name, T1.h_name, Kingdom.name as k_name, T1.motherland \
from (SELECT Character.name, Character.motherland ,House.name as h_name ,House.id_kingdom \
FROM Character JOIN House  \
on Character.id_house = House.id_house where Character.id_character = " + str(id_c) + ") as T1 \
join Kingdom on Kingdom.id_kingdom = T1.id_kingdom where T1.id_kingdom = Kingdom.id_kingdom;"
    cur.execute(query)
    result = cur.fetchone()
    data = [["Имя", "Название дома", "Название королевства"]]
    data.append([])
    for x in result:
        data[1].append(x)
    win.model = TableModel(data)
    win.table.setModel(win.model)
    i = 0
    for x in data[0]:
        win.table.setColumnWidth(i, 160)
        i+=1
    win.table.show()

def otv_f(win):
    query = "WITH CTE (id, population_n) AS\
    (SELECT id_kingdom, population\
    FROM Kingdom\
    GROUP BY id_kingdom)\
SELECT AVG(population_n) as AVG_POPYLATION FROM CTE;"
    cur.execute(query)
    result = cur.fetchone()
    data = [["Среднее население по всем королевствам"],[float(result[0])]]
    win.model = TableModel(data)
    win.table.setModel(win.model)
    win.table.setColumnWidth(0, 300)
    win.table.show()

def meta_f(win):
    query = "SELECT pg_database.oid\
        FROM pg_database\
    WHERE pg_database.datname = 'Game_of_Thrones';"
    cur.execute(query)
    result = cur.fetchone()
    data = [["ID DB"],[float(result[0])]]
    win.model = TableModel(data)
    win.table.setModel(win.model)
    win.table.show()

def scalar_func_f(win):
    if win.flag_scalar_func:

        query = "CREATE OR REPLACE FUNCTION GetAvgCastelsPopulation(id INT)\
    RETURNS INT AS $$\
    BEGIN\
        RETURN (SELECT AVG(population) FROM Castle WHERE id_kingdom = id and type = 'Замок');\
    END;\
    $$ LANGUAGE PLPGSQL;"
        cur.execute(query)
        win.flag_scalar_func = False

    query = "SELECT name, GetAvgCastelsPopulation(id_kingdom) FROM Kingdom;"
    cur.execute(query)
    result = cur.fetchall()
    data = [["Королевство", "Среднее население в замках"]]

    for x in result:
        tmp = []
        for y in x:
            tmp.append(y)
        data.append(tmp)
    win.model = TableModel(data)
    win.table.setModel(win.model)
    win.table.setColumnWidth(0, 180)
    win.table.setColumnWidth(1, 220)
    win.table.show()

def table_func_f(win):
    if win.flag_table_func:

        query = "CREATE FUNCTION GetOrganizationInfo(id_c int)\
RETURNS TABLE \
    (character_name VARCHAR,\
     organization_name VARCHAR,\
     year_in VARCHAR\
    ) AS $$\
BEGIN \
    DROP TABLE IF EXISTS DETECTED_STAT;\
    CREATE TEMP TABLE DETECTED_STAT(\
     character_name VARCHAR,\
     organization_name VARCHAR,\
     year_in VARCHAR    \
    );\
    INSERT INTO DETECTED_STAT(character_name, organization_name, year_in)\
    SELECT T.name, Organization.name, T.years_in\
    FROM Organization\
        JOIN\
    (SELECT Character.name, organ_and_charac.id_organization, organ_and_charac.years_in\
     FROM Character JOIN organ_and_charac \
     on Character.id_character = organ_and_charac.id_character where Character.id_character = id_c) as T\
     on T.id_organization = Organization.id_organization;\
     \
     RETURN query SELECT * FROM DETECTED_STAT;\
END;\
$$ LANGUAGE PLPGSQL;"
        cur.execute(query)
        win.flag_table_func = False

    id_c = win.spinBox_table.value()
    query = "SELECT * FROM GetOrganizationInfo("+ str(id_c)+");"
    cur.execute(query)
    result = cur.fetchall()
    data = [["Имя", "Организация", "Проведенные годы"]]

    for x in result:
        tmp = []
        for y in x:
            tmp.append(y)
        data.append(tmp)
    win.model = TableModel(data)
    win.table.setModel(win.model)
    win.table.setColumnWidth(0, 180)
    win.table.setColumnWidth(1, 150)
    win.table.setColumnWidth(2, 150)
    win.table.show()

def proc_f(win):
    if win.flag_proc:

        query = "CREATE OR REPLACE PROCEDURE ChangePersonStatus(id INT, n_alive BOOL)\
AS $$\
BEGIN \
    UPDATE Character\
    SET alive = n_alive\
    WHERE Character.id_character = id;\
END;\
$$ LANGUAGE PLPGSQL;"
        cur.execute(query)
        win.flag_proc = False

    id_c = win.spinBox_proc.value()
    state = win.checkBox_proc.isChecked()

    query = "CALL ChangePersonStatus("+str(id_c)+", "+ str(state) +");"
    cur.execute(query)
    query = "select * from character where id_character = "+str(id_c)+";"
    cur.execute(query)
    result = cur.fetchall()
    columns = cur.description
    data = [["id", "Имя", "Пол", "Культура", "Титул", "Родина", "Возраст", "Статус"]]

    for x in result:
        tmp = []
        for y in x:
            tmp.append(y)
        data.append(tmp)
    win.model = TableModel(data)
    win.table.setModel(win.model)

def sys_f(win):
    query = "select current_user;"
    cur.execute(query)
    result = cur.fetchone()
    data = [["Имя пользователя"],[result[0]]]
    win.model = TableModel(data)
    win.table.setModel(win.model)
    win.table.setColumnWidth(0, 220)
    win.table.show()

def create_f(win):
    flag = False
    query = "CREATE TABLE Wars\
(\
    Id_war serial primary key NOT NULL,\
    id_house_1 int NOT NULL,\
    id_house_2 int NOT NULL,\
    years int NOT NULL,\
    deaths int NOT NULL,\
    Foreign key (Id_house_1) references House (Id_house),\
    Foreign key (Id_house_2) references House (Id_house)\
);"
    cur.execute(query)
    
    data = [["Создана новая таблица"]]
    win.model = TableModel(data)
    win.table.setModel(win.model)
    win.table.setColumnWidth(0, 220)
    win.table.show()

def insert_f(win):

    if (flag)
        return
    id_1 = win.spinBox.value()
    id_2 = win.spinBox_2.value()
    years = win.spinBox_3.value()
    deths = win.spinBox_4.value()
    

    query = "INSERT INTO Wars(id_house_1, id_house_2, years, deaths)\
VALUES(" + str(id_1) +", " + str(id_2) +"," + str(years) +"," + str(deths) +");"
    cur.execute(query)

    query = "select * from Wars;"
    cur.execute(query)

    result = cur.fetchall()
    data = [["id","Дом 1", "Дом 2", "Годы", "Смерти"]]

    for x in result:
        tmp = []
        for y in x:
            tmp.append(y)
        data.append(tmp)
    win.model = TableModel(data)
    win.table.setModel(win.model)
    win.table.setColumnWidth(0, 180)
    win.table.setColumnWidth(1, 220)
    win.table.show()




conn = db.connect(database="Game_of_Thrones", user="postgres", password="1234", host="localhost", port=5432)
cur = conn.cursor()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec())