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

# uic.loadUiType(ui파일경로)
#   - XML 언어로 작성된 ui파일을 읽어서 파이썬 클래스 코드를 만드는 기능
#   - MyWindow 클래스가 inherit 받는 class 중 하나
#   - from PyQt5 import uic를 해줘야 한다.


# form_class.setupUi()
#   - qt designer에서 만든 클래스들을 초기화 해주는 기능


# qt designer에서 widget을 클릭하면 '속성 편집기'의 object name 항목에
# 이벤트 해당 widget 객체를 바인딩하는 변수이름을 확인할 수 있다.
# 이 변수명은 이벤트 처리하는 메서드를 연결할 때 정확히 기재해야 한다.

