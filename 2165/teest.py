# 6894556/1665/03.28.py를 참고하여 test.py 수정

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class MySignal(QObject):
    signal1 = pyqtSignal()
    signal2 = pyqtSignal(int, int)

    def run(self):
        self.signal1.slot1()
        self.signal2.slot2(1, 2)

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        mysignal = MySignal()
        mysignal.signal1.connect(self.slot1)
        mysignal.signal2.connect(self.slot2)
        mysignal.run()

    def initUI(self):
        lcd = QLCDNumber(self)
        # lbl = QLabel('label', self)
        btn1 = QPushButton('1', self)
        btn2 = QPushButton('+', self)
        btn3 = QPushButton('=', self)


        hbox = QHBoxLayout()
        hbox.addWidget(btn1)
        hbox.addWidget(btn2)
        hbox.addWidget(btn3)

        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        # vbox.addWidget(lbl)
        vbox.addLayout(hbox)

        self.setLayout(vbox)



        # btn1.clicked.connect(self.slot1)    # btn1 -> lcd
        # btn2.clicked.connect(self.slot2)    # btn2 -> lcd
        # btn3.clicked.connect(self.slot1)    # btn3 -> lcd


        self.setWindowTitle('')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    @pyqtSlot()
    def slot1(self):
        print('slot1')

    @pyqtSlot(int, int)
    def slot2(self, arg1, arg2):
        print('slot2', arg1, arg2)

    def slot3(self):
        return 0

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())

# modules of PyQt5 : https://www.riverbankcomputing.com/static/Docs/PyQt5/module_index.html#ref-module-index
# QtWidgets : https://www.riverbankcomputing.com/static/Docs/PyQt5/api/qtwidgets/qtwidgets-module.html
# QLCDNumer : https://www.riverbankcomputing.com/static/Docs/PyQt5/api/qtwidgets/qlcdnumber.html?highlight=qlcdnumber#QLCDNumber