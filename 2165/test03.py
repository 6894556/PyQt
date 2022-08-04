import sys
from PyQt5.QtWidgets import (QApplication, QWidget,
                             QPushButton, QLCDNumber, QLabel,
                             QVBoxLayout, QHBoxLayout)

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.turn=0
        self.initUI()

    def initUI(self) -> object:
        self.lcd1 = QLCDNumber(self)
        self.label1 = QLabel(self)
        self.lcd3 = QLCDNumber(self)
        self.lcd4 = QLCDNumber(self)

        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.lcd1)
        hbox1.addWidget(self.label1)
        hbox1.addWidget(self.lcd3)
        hbox1.addWidget(self.lcd4)

        # lbl = QLabel('label', self)
        btn1 = QPushButton('1', self)
        btn2 = QPushButton('+', self)
        btn3 = QPushButton('=', self)


        hbox = QHBoxLayout()
        hbox.addWidget(btn1)
        hbox.addWidget(btn2)
        hbox.addWidget(btn3)

        vbox = QVBoxLayout()
        #vbox.addWidget(self.lcd)
        vbox.addLayout(hbox1)
        # vbox.addWidget(lbl)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        btn1.clicked.connect(self.slot1)    # btn1 -> lcd
        btn2.clicked.connect(self.slot2)    # btn2 -> lcd
        btn3.clicked.connect(self.slot3)    # btn3 -> lcd


        self.setWindowTitle('')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def slot1(self):
        self.turn = self.turn+1
        if self.turn>1:
            self.lcd3.display(1)
        else:
            self.lcd1.display(1)
        return

    def slot2(self):
        self.label1.setText('+')
        return

    def slot3(self):
        self.turn=0
        operand1=self.lcd1.value()
        operand2=self.lcd3.value()
        operator = self.label1.text()
        print(operator)
        if operator=='+':
            r = int(operand1) + int(operand2)
            self.lcd4.display(r)
        return

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())