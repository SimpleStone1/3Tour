import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem
from PyQt5.QtGui import QPen,QBrush,QColor

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor,QPen

import sqlite3 as sq

class Ui_Form(object):
    def __init__(self):
        super().__init__()
        self.db_name = '3tour.db'
        self.rectangles = {}
        self.table = ['ID', 'X1', 'Y1', 'X2', 'Y2']
        self.tables = {0: 'ID', 1: 'X1', 2: 'Y1', 3: 'X2', 4: 'Y2'}
    
    def create(self):
        try:
            with sq.connect(self.db_name) as con:
                cur = con.cursor()
                cur.execute("""
                    CREATE TABLE IF NOT EXISTS RECTANGLES(
                                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                                X1 REAL,
                                Y1 REAL,
                                X2 REAL,
                                Y2 REAL
                                )
                """)
                con.commit()
        except Exception as e:
            print(f'Ошибка БД {e}')

    def load(self):
        try:
            with sq.connect(self.db_name) as con:
                cur = con.cursor()
                cur.execute("""
                    SELECT * FROM RECTANGLES
                """)
                lines = cur.fetchall()
                for line  in enumerate(lines):
                    self.rectangles[line[0]] = line[1]
                    x1 = line[1][1]
                    x2 = line[1][2]
                    y1 = line[1][3]
                    y2 = line[1][4]
                    self.create_rect(self,x1,y1,x2 - x1,y2 - y1)
        except Exception as e:
            print(f'Ошибка БД {e}')
    def add_item(self, id, x1= None, y1 = None, x2 = None, y2 = None):
        try:
            with sq.connect(self.db_name) as con:
                cur = con.cursor()
                cur.execute("""
                    INSERT OR IGNORE INTO RECTANGLES VALUES (?, ?, ?, ?, ?)
                """, (id, x1, y1, x2, y2))
                con.commit()
            self.create_rect(self,x1,y1,x2 - x1,y2 - y1)
        except Exception as e:
            print(f'Ошибка БД {e}')
    
    def delete(self, id):
        try:
            with sq.connect(self.db_name) as con:
                cur = con.cursor()
                cur.execute("""
                    DELETE FROM RECTANGLES WHERE ID = ?
                """, (id,))
        except Exception as e:
            print(f'Ошибка БД {e}')

    def exists(self, id):
        try:
            with sq.connect(self.db_name) as con:
                cur = con.cursor()
                cur.execute("SELECT EXISTS(SELECT 1 FROM RECTANGLES WHERE ID = ?)", (id,))
                exists = cur.fetchone()[0]
                return exists
        except Exception as e:
            print(f'Ошибка БД {e}')

    def update(self, id, x1=None, y1=None, x2=None, y2=None):
        try:
            with sq.connect(self.db_name) as con:
                cur = con.cursor()
                updates = []
                params = []
                if x1 is not None:
                    updates.append("X1 = ?")
                    params.append(x1)
                if y1 is not None:
                    updates.append("Y1 = ?")
                    params.append(y1)
                if x2 is not None:
                    updates.append("X2 = ?")
                    params.append(x2)
                if y2 is not None:
                    updates.append("Y2 = ?")
                    params.append(y2)
                
                if not updates:
                    return
                query = f"UPDATE RECTANGLES SET {', '.join(updates)} WHERE ID = ?"
                params.append(id)
                cur.execute(query, params)
                con.commit()
        except Exception as e:
            print(f'Ошибка БД при обновлении: {e}')
            
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1144, 827)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 601, 731))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0) 

        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(610, 0, 531, 781))
        self.graphicsView.setObjectName("graphicsView")

        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 740, 591, 30))
        self.widget.setObjectName("widget")

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)

        self.add_new_object = QtWidgets.QPushButton(self.widget)
        self.horizontalLayout.addWidget(self.add_new_object)

        self.delet_select_object = QtWidgets.QPushButton(self.widget)
        self.horizontalLayout.addWidget(self.delet_select_object)

        self.calculate_button = QtWidgets.QPushButton(self.widget)
        self.horizontalLayout.addWidget(self.calculate_button)

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1144, 26))
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.scene = QtWidgets.QGraphicsScene(self.graphicsView)
        self.graphicsView.setScene(self.scene)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tableWidget.setHorizontalHeaderLabels(['ID', 'X1', 'Y1', 'X2', 'Y2'])
        self.add_new_object.setText(_translate("MainWindow", "Добавить новый объект"))
        self.delet_select_object.setText(_translate("MainWindow", "Удалить выбранный объект"))
        self.calculate_button.setText(_translate("MainWindow", "Рассчитать"))

    def load_to_table(self):
        try:
            with sq.connect(self.db_name) as con:
                cur = con.cursor()
                cur.execute("SELECT * FROM RECTANGLES")
                rows = cur.fetchall()
                
                self.tableWidget.blockSignals(True)
                self.tableWidget.setRowCount(0) 
                
                for row_data in rows:
                    row_number = self.tableWidget.rowCount()
                    self.tableWidget.insertRow(row_number)
                    for column_number, data in enumerate(row_data):
                        self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))
                
                self.tableWidget.blockSignals(False)
        except Exception as e:
            print(f'Ошибка загрузки: {e}')

    def update_db_field(self, row, column):
        if column == 0: return 

        item = self.tableWidget.item(row, column)
        id_item = self.tableWidget.item(row, 0)

        if item and id_item:
            val = item.text()
            rect_id = id_item.text()
            field_name = self.tables.get(column)
            
            try:
                with sq.connect(self.db_name) as con:
                    cur = con.cursor()
                    cur.execute(f"UPDATE RECTANGLES SET {field_name} = ? WHERE ID = ?", (val, rect_id))
                    con.commit()
                    print(f"Обновлено: ID {rect_id}, {field_name} = {val}")
            except Exception as e:
                print(f"Ошибка обновления БД: {e}")

    def add_row_to_db(self):
        try:
            with sq.connect(self.db_name) as con:
                cur = con.cursor()
                cur.execute("INSERT INTO RECTANGLES (X1, Y1, X2, Y2) VALUES (0, 0, 0, 0)")
                con.commit()
                self.load_to_table()
        except Exception as e:
            print(f"Ошибка добавления: {e}")

    def functions(self):
        self.tableWidget.cellChanged.connect(self.update_db_field)
        self.add_new_object.clicked.connect(self.add_row_to_db)

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        black = QPen(Qt.black,3)
        ser = QColor(0,0,0,120)
        white = QColor(255,255,255,255)
        self.ui.scene.setBackgroundBrush(white)
        for  i in range(10):
            mnog=i*50
            self.ui.scene.addLine(0+mnog,1000,0+mnog,-1000,ser)
            self.ui.scene.addLine(0-mnog,1000,0-mnog,-1000,ser)
            self.ui.scene.addLine(-1000,0-mnog,1000,0-mnog,ser)
            self.ui.scene.addLine(-1000,0+mnog,1000,0+mnog,ser)

        self.ui.scene.addLine(-1000,0,1000,0,black)
        self.ui.scene.addLine(0,-1000,0,1000,black)

app = QApplication(sys.argv)
w = MainWindow()
w.ui.create()
w.ui.load_to_table()
w.ui.functions()
w.show()
app.exec_()