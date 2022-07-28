# # qt designer 7
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
import pykorbit
# 비트코인 현재가를 statusBar에 자동으로 1초마다 갱신해서 출력하는 프로그램

form_class = uic.loadUiType("window_03_26.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setGeometry(100, 100, 500, 500)

        self.timer = QTimer(self)
        self.timer.start(1000)
        self.timer.timeout.connect(self.inquiry)

    def inquiry(self):
        cur_time = QTime.currentTime()
        str_time = cur_time.toString("hh:mm:ss")
        # showmessage가 아니라 showMessage이다.
        self.statusBar().showMessage(str_time)
        price = pykorbit.get_current_price("BTC")
        self.lineEdit.setText(str(price))

app = QApplication([])
window = MyWindow()
window.show()
app.exec_()