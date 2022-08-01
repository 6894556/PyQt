# pyqt 윈도우 꾸미기 2
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 300, 300)
        self.setWindowTitle("PyQt")
        self.setWindowIcon(QIcon("saturn.png"))

app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()


# QMainWindow.setTitle(제목)
#   - str 제목
#   - default 'python'

# QIcon
#   - QIcon 클래스는 QtGui 파일에 있으므로 QtGui파일을 불러와야 한다(from PyQt5.QtGui import *)
#   - 16 by 16 png format의 아이콘 파일
#   - 프로그램의 특징을 잘 보여주는 그림이 좋음

# QMainWindow.setWindowIcon(QIcon(아이콘 파일 경로))
#   - window의 icon을 자신이 원하는 이미지로 변경

