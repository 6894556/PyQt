from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class MySignal(QObject):
    signal1 = pyqtSignal()
    signal2 = pyqtSignal(int, int)

    def run(self):
        self.signal1.emit()
        self.signal2.emit(1, 2)


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        mysignal = MySignal()
        mysignal.signal1.connect(self.signal1_emitted)
        mysignal.signal2.connect(self.signal2_emitted)
        mysignal.run()

    @pyqtSlot()
    def signal1_emitted(self):
        print("signal1 emitted")

    @pyqtSlot(int, int)
    def signal2_emitted(self, arg1, arg2):
        print("signal2 emitted", arg1, arg2)


app = QApplication([])
window = MyWindow()
window.show()
app.exec_()


# 시그널이 발생하면 이벤트 루프가 미리 정의된 슬롯으로 시그널로부터 온 값을 보내준다.
# signal2.emit(1, 2)의 int값 두개를 이벤트 루프가 ignal2_emitted(1, 2)와 슬롯에게 넘겨준다.


