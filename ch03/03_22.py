from PyQt5.QtWidgets import *
from PyQt5 import uic
import pykorbit  # 파이썬이 있는 상태에서 아나콘다를 설치해서 인터프리터를 콘다 파이썬으로 설정하지 않음
# -> 그래서 pykorbit 실습 못함

form_class = uic.loadUiType("mywindow.ui")[0]


class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.inquiry)

    def inquiry(self):
        print("조회 버튼 클릭")

app = QApplication([])
window = MyWindow()
window.show()
app.exec_()