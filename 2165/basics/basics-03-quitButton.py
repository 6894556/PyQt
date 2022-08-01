## Ex 3-3 : 창 닫기 버튼 만들기

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import QCoreApplication

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btn = QPushButton("Quit", self)
        btn.move(50, 50)
        btn.resize(btn.sizeHint())
        btn.clicked.connect(QCoreApplication.instance().quit)

        self.setWindowTitle("Quit Button")
        self.setGeometry(300, 300, 300, 200)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())


# 버튼 'btn'을 클릭하면 'clicked'시그널이 만들어진다. -- 1
# 'quit' 슬롯이 call 되면 어플리케이션이 종료된다. -- 2)

# 시그널이 발생하면 연결된 슬롯이 call 된다.
# 'clicked' 시그널은 'quit' 슬롯에 연결되어 있다.
# 따라서 'clicked' 시그널이 발생하면 'quit' 슬롯이 call 된다.

# 그러므로 버튼 'btn'을 클릭하면 'quit' 슬롯이 call 된다. -- 1*
# 고로 버튼 'btn'을 클릭하면 어플리케이션이 종료된다. -- 2*

# Sender -> Reciver : btn  -> 어플리케이션

# QPushButton : https://www.riverbankcomputing.com/static/Docs/PyQt5/api/qtwidgets/qpushbutton.html