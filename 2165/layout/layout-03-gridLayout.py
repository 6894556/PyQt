# Ex 4-3 : 그리드 레이아웃

import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QGridLayout, QLabel,
                             QLineEdit, QTextEdit)

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)

        # 3행 2열 그리드 레이아웃
        # n행 m열 그리드 레이아웃 만드는 함수 작성이 가능할까?

        grid.addWidget(QLabel('Title:'), 0, 0) # 0번행 0번열
        grid.addWidget(QLabel('Autuor:'), 1, 0) # 1번행 0번열
        grid.addWidget(QLabel('Review:'), 2, 0)

        grid.addWidget(QLineEdit(), 0, 1)
        grid.addWidget(QLineEdit(), 1, 1)
        grid.addWidget(QLineEdit(), 2, 1)

        self.setWindowTitle('QGridLayout')
        self.setGeometry(300, 300, 300, 200)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())

