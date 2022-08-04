from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic


form_class = uic.loadUiType("calculator_01.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setGeometry(300, 300, 600, 600)
        self.setWindowTitle("calculator")
        self.setWindowIcon(QIcon("calculator.png"))

        self.pushButton_15.clicked.connect(self.btn_clicked)

    def btn_clicked(self):
        self.lcdNumber.display(1)





app = QApplication([])
window = MyWindow()
window.show()
app.exec_()

