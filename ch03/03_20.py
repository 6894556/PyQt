# qt designer 1
from PyQt5.QtWidgets import *
from PyQt5 import uic

# Qt Designer.exe로 mywindow.ui파일을 제작하고
# 03_20.py와 동일한 디렉토리로 이동시킨 상태로 아래 코드를 작성

form_class = uic.loadUiType("mywindow.ui")[0]


class Mywindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


app = QApplication([])
window = Mywindow()
window.show()
app.exec_()

# Qc Designer
#   - 드래그 앤 드롭으로 윈도우에 위젯을 추가해서 UI 파일을 만드는 응용프로그램
#   - anaconda3/Library/bin/designer.exe
#   - 미리보기 단축키 : Ctrl + R

#  Qc Designer로 제작한 UI를 사용하기 위해 필요한 두 가지
#   1. uic.loadUiType("UI파일 경로")[0] : UI파일을 읽어서 파이썬 클래스로 만들어 주는 메서드 (from PyQt5 import uic 필요)
#   2. setupUi() : Qt Designer에서 만든 클래스들을 초기화 해주는 메서드