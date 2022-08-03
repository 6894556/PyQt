# Ex 5-2 : QLabel

import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QVBoxLayout)
from PyQt5.QtCore import Qt

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
       label1 = QLabel('First Lable', self)
       label1.setAlignment(Qt.AlignCenter)

       label2 = QLabel('Second Lable', self)
       label2.setAlignment(Qt.AlignVCenter)

       font1 = label1.font()
       font1.setPointSize(20)

       font2 = label2.font()
       font2.setFamily('Times New Roman')
       font2.setBold(True)

       layout = QVBoxLayout()
       layout.addWidget(label1)
       layout.addWidget(label2)

       self.setLayout(layout)

       self.setWindowTitle('QLabel')
       self.setGeometry(300, 300, 300, 200)
       self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())


# QLabel(라벨 텍스트, 부모위젯)
# QLabel.setAlignment() : 라벨의 배치 설정
# Qt.ALignCenter : 수평, 수직 방향 모두 가운데 위치
# Qt.AlignHCenter : 수평 방향 가운데로 설정
# Qt.AlignVCenter : 수직 방향 가운데로 설정