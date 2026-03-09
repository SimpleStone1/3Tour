import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor

class Ui_Form(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1144, 827)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 601, 731))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(1)

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)

        for i in range(5):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(i, item)

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
        self.tableWidget.verticalHeaderItem(0).setText(_translate("MainWindow", "1"))
        self.tableWidget.horizontalHeaderItem(0).setText(_translate("MainWindow", "ID"))
        self.tableWidget.horizontalHeaderItem(1).setText(_translate("MainWindow", "X1"))
        self.tableWidget.horizontalHeaderItem(2).setText(_translate("MainWindow", "Y1"))
        self.tableWidget.horizontalHeaderItem(3).setText(_translate("MainWindow", "X2"))
        self.tableWidget.horizontalHeaderItem(4).setText(_translate("MainWindow", "Y2"))
        self.add_new_object.setText(_translate("MainWindow", "Добавить новый объект"))
        self.delet_select_object.setText(_translate("MainWindow", "Удалить выбранный объект"))
        self.calculate_button.setText(_translate("MainWindow", "Рассчитать"))


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)


        white = QColor(255,255,255,255)
        self.ui.scene.setBackgroundBrush(white)
        



app = QApplication(sys.argv)
w = MainWindow()
w.show()
sys.exit(app.exec_())