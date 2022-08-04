# # qt designer 5
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import *
import pykorbit

form_class = uic.loadUiType("window_03_24.ui")[0]


class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.inquiry)

        self.setWindowTitle('비트코인 현재 가격 조회')
        self.setWindowIcon(QIcon("coin.jpg"))
        self.setGeometry(300, 300, 300, 300)

    def inquiry(self):
        price = pykorbit.get_current_price("BTC")
        self.lineEdit.setText(str(price))

app = QApplication([])
window = MyWindow()
window.show()
app.exec_()

