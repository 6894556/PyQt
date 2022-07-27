# # pyqt 윈도우 꾸미기 4

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(0,0, 300, 300)
        self.setWindowTitle("PyQt")
        self.setWindowIcon(QIcon("saturn.png"))

        btn1 = QPushButton("버튼1", self)
        btn1.move(10, 10)

        btn2 = QPushButton("버튼2", self)
        btn2.move(10, 40)

app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()

# QPushButton.move(ax, ay)
#   - window 내에서 버튼의 위치를 (ax, ay)로 변경
#   - 버튼이 두개 이상일 경우 필요(두 버튼 위치가 같으면 하나가 보이지 않는 문제)

# 버튼이 두개 이상일 경우 instance를 바이딩하는 변수의 이름이 중복되지 않도록 주의할 것