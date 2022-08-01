# pyqt 기초 3

import sys
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow):
    def __init__(self):
        # superclass의 constructor를 호출
        # 이유 : PyQt가 제공하는 클래스(QMainWindow)를 inherit 하는 경우
        #       superclass의 constructor를 호출해야 하기 때문
        super().__init__()

app = QApplication(sys.argv)

window = MyWindow()
window.show()

app.exec_()


# QMainWindow로부터 inherit 받아야
# QMainWindow의 method(e.g. QMainWidow.show())를 사용할 수 있다.
