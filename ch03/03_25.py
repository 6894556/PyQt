# # qt designer 6
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic

# 윈도우 상태바에 얻어온 현재 시간을 출력하는 프로그램

form_class = uic.loadUiType("window_03_25.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 500, 500)
        # QTimer 객체를 만들고 interval 1초로 설정
        # interval : 얼마나 자주 이벤트가 발생하는지를 의미
        self.timer = QTimer(self)
        self.timer.start(1000)
        # QTimer의 'timeout'이벤트
        # timeout 이벤트 : 설정한 interval마다 발생하는 이벤트
        # interval을 1초로 설정한 QTimer 객체를 만들고
        # 1초에 한 번씩 timeout이벤트가 발생하고 이벤트 루프는
        # 1초에 한번씩 self.timeout()이라는 메서드를 호출한다.
        self.timer.timeout.connect(self.timeout)

    def timeout(self):
        cur_time = QTime.currentTime()
        str_time = cur_time.toString("hh:mm:ss")
        self.statusBar().showMessage(str_time)

app = QApplication([])
window = MyWindow()
window.show()
app.exec_()