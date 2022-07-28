# # qt designer 6
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic

form_class = uic.loadUiType("window_03_25.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 500, 500)
        # QTimer 객체를 만들고 interval 1초로 설정
        # interval : 얼마나 자주 이벤트가 발생하는지를 의미
        self.timer = QTimer(self)
        self.timer.start(1000)
        self.timer.timeout.connect(self.timeout)

    def timeout(self):
        cur_time = QTime.currentTime()
        str_time = cur_time.toString("hh:mm:ss")
        self.statusBar().showMessage(str_time)

app = QApplication([])
window = MyWindow()
window.show()
app.exec_()



# QTimer

# QTimer.start(interval)
# QTimer.timeout.connect(method) : interval이 1000일 경우 1초에 한번 method 호출 (timeout 이벤트)

# QTime.currentTime() : 현재 시간