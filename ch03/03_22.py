# # qt designer 3
# qtDesigner로 만든 ui파일을 불러와서 버튼에 clicked 이벤트를 처리하는 메서드 inquiry 연결
from PyQt5.QtWidgets import *
from PyQt5 import uic


form_class = uic.loadUiType("window_03_22.ui")[0]


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