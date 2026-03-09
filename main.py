import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget



class Main(QMainWindow):
    def __init__(self):
        super().__init__()













if __name__ == '__main__':
    app = QApplication(sys.argv)
    wind = Main()
    wind.show()
    app.exec_()

