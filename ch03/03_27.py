from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class Mysignal(QObject):
    signal1 = pyqtSignal()

    def run(self):
        self.signal1.emit()

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        mysignal = Mysignal()
        mysignal.signal1.connect(self.signal1_emitted)
        mysignal.run()

    @pyqtSlot()
    def signal1_emitted(self):
        print("signal1 emitted")

app = QApplication([])
window = MyWindow()
window.show()
app.exec_()


# signal : 위젯에 정의된 이벤트
# slot : signal이 발생할 때 호출되는 메서드

# 이 코드에서 signal 정의한 방법
#   1. MySignal 클래스 정의
#   2. MySignal 클래스에서 pyqtSignal 객체 생성
#   3. pyqtSignal 객체를 바인딩하고 있는 클래스 변수 signal1이 정의한 signal(이벤트)의 이름

# pyqtSignal.emit() :

# slot을 직접 정의한 signal에 연결하는 방법
#   - 직접 정의한 signal 이름 : signal1
#   - 연결 : signal1.connect(self.slot이름)
#   - slot이 호출되는 경우 : signal1이 발생했을 때

# 직접 정의한 signal1이 발생하는 순간
#   - run()이 호출되면서 emit()이 호출될 때 signal1이 발생

# @pyqtSlot(데커레이터) : 시그널과 슬롯을 연결할 때 데커레이터를 적어주면 더 좋다.