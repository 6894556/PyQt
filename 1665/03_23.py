# # qt designer 4
from PyQt5.QtWidgets import *
from PyQt5 import uic
import pykorbit

# 조회버튼을 클릭하면 비트코인 현재가를 콘솔에 출력

form_class = uic.loadUiType("window.ui")[0]


class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.inquiry)

    def inquiry(self):
        price = pykorbit.get_current_price("BTC")
        print(price)

app = QApplication([])
window = MyWindow()
window.show()
app.exec_()

