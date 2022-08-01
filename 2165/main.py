import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QDesktopWidget, QVBoxLayout, QGridLayout,
                             QLineEdit, QPushButton)
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)

        ''' QLineEdit을 add 하지 못함
        vbox = QVBoxLayout()
        vbox.addStretch(3)

        vbox.addWidget(QLineEdit.setText('calculation result'))
        vbox.addLayout(grid)
        self.setLayout(vbox)
        '''

        # grid.addWidget(QLineEdit.setText('calculation result'), 0, 0)
        grid.addWidget(QPushButton('('), 1, 0)
        grid.addWidget(QPushButton(')'), 1, 1)
        grid.addWidget(QPushButton('%'), 1, 2)
        grid.addWidget(QPushButton('AC'), 1, 3)
        grid.addWidget(QPushButton('7'), 2, 0)
        grid.addWidget(QPushButton('8'), 2, 1)
        grid.addWidget(QPushButton('9'), 2, 2)
        grid.addWidget(QPushButton('/'), 2, 3)
        grid.addWidget(QPushButton("4"), 3, 0)
        grid.addWidget(QPushButton("5"), 3, 1)
        grid.addWidget(QPushButton("6"), 3, 2)
        grid.addWidget(QPushButton("x"), 3, 3)
        grid.addWidget(QPushButton("1"), 4, 0)
        grid.addWidget(QPushButton("2"), 4, 1)
        grid.addWidget(QPushButton("3"), 4, 2)
        grid.addWidget(QPushButton("-"), 4, 3)
        grid.addWidget(QPushButton("0"), 5, 0)
        grid.addWidget(QPushButton("."), 5, 1)
        grid.addWidget(QPushButton("="), 5, 2)
        grid.addWidget(QPushButton("+"), 5, 3)

        self.resize(200, 500)
        self.setWindowTitle("GUI Calculator")
        self.setWindowIcon(QIcon('calculator.png'))
        self.center()
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())


# QLineEdit : https://www.riverbankcomputing.com/static/Docs/PyQt5/api/qtwidgets/qlineedit.html
#