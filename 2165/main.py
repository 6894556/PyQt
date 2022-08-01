import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import QCoreApplication

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btn_00 = QPushButton("(", self)
        btn_01 = QPushButton(")", self)
        btn_02 = QPushButton("%", self)
        btn_03 = QPushButton("AC", self)
        btn_10 = QPushButton("7", self)
        btn_11 = QPushButton("8", self)
        btn_12 = QPushButton("9", self)
        btn_13 = QPushButton("/", self)
        btn_20 = QPushButton("4", self)
        btn_21 = QPushButton("5", self)
        btn_22 = QPushButton("6", self)
        btn_23 = QPushButton("x", self)
        btn_30 = QPushButton("1", self)
        btn_31 = QPushButton("2", self)
        btn_32 = QPushButton("3", self)
        btn_33 = QPushButton("-", self)
        btn_40 = QPushButton("0", self)
        btn_41 = QPushButton(".", self)
        btn_42 = QPushButton("=", self)
        btn_43 = QPushButton("+", self)

        self.setWindowTitle("GUI Calculator")
        self.move(300, 300)
        self.resize(400, 200)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())