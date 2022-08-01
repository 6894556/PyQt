# pyqt 윈도우 꾸미기 3
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(0,0, 300, 300)
        self.setWindowTitle("PyQt")
        self.setWindowIcon(QIcon("saturn.png"))
        # self라는 변수가 window를 바인딩하고 있으므로 self를 넘겨준다?
        btn = QPushButton("버튼1", self)


app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()

# constructor는 instance가 생성될 때 자동으로 호출 된다.
# 따라서 버튼을 window에 추가하고 싶으면 constructor에 추가하면 된다.
