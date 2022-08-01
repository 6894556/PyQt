# pyqt 윈도우 꾸미기 1
import sys
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 500, 1000)

app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()


# QMainWindow.setGeometry(ax:int, ay:int, aw:int, ah:int)
#   1. window 위치 지정 : ax, ay
#   2. window 크기 지정 : aw, ah
