import sys
from PyQt5.QtWidgets import (QApplication, QWidget,
                             QPushButton, QLCDNumber, QLabel,
                             QVBoxLayout, QHBoxLayout)

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.turn = 0   # ?
        self.initUI()

    def initUI(self) -> object:
        self.display1 = QLCDNumber(self)
        self.display2 = QLabel(self)
        self.display3 = QLCDNumber(self)
        self.display4 = QLCDNumber(self)

        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.display1)
        hbox1.addWidget(self.display2)
        hbox1.addWidget(self.display3)
        hbox1.addWidget(self.display4)

        btn1 = QPushButton('1', self)
        btn2 = QPushButton('+', self)
        btn3 = QPushButton('=', self)

        hbox2 = QHBoxLayout()
        hbox2.addWidget(btn1)
        hbox2.addWidget(btn2)
        hbox2.addWidget(btn3)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)

        self.setLayout(vbox)

        btn1.clicked.connect(self.slot1)    # btn1 -> lcd
        btn2.clicked.connect(self.slot2)    # btn2 -> lcd
        btn3.clicked.connect(self.slot1)    # btn3 -> lcd


        self.setWindowTitle('')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def slot1(self):
        self.turn = self.turn + 1
        if self.turn > 1:
            self.display3.display(1)
        else:
            self.display1.display(1)


    def slot2(self):
        self.display2.setText('+')

    def slot3(self):
        self.turn = 0
        operand1 = self.display1.value()
        operator = self.display2.text()
        operand2 = self.display3.value()
        print(operator)
        if operator == '+':
            rst = int(operand1) + int(operand2)
            self.display4.display(rst)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())

# modules of PyQt5 : https://www.riverbankcomputing.com/static/Docs/PyQt5/module_index.html#ref-module-index
# QtWidgets : https://www.riverbankcomputing.com/static/Docs/PyQt5/api/qtwidgets/qtwidgets-module.html
# QLCDNumer : https://www.riverbankcomputing.com/static/Docs/PyQt5/api/qtwidgets/qlcdnumber.html?highlight=qlcdnumber#QLCDNumber