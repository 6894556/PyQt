# # qt designer 5
from PyQt5.QtWidgets import *
from PyQt5 import uic
import pykorbit

# 조회버튼 클릭하면 QLineEdit 위젯에 출력

form_class = uic.loadUiType("window_03_24.ui")[0]


class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.inquiry)

    def inquiry(self):
        price = pykorbit.get_current_price("BTC")
        self.lineEdit.setText(str(price))

app = QApplication([])
window = MyWindow()
window.show()
app.exec_()