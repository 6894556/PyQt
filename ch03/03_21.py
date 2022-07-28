# # qt designer 2
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("mywindow.ui")[0]


class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.btn_clicked) # object name : pushButton

    def btn_clicked(self):
        print("버튼 클릭")

app = QApplication([])
window = MyWindow()
window.show()
app.exec_()

# Qt Designer로 생성한 widget의 이벤트 처리하기 위해서는
# Qc Desinger의 객체 탐색기/object name을 확인해야 한다.

