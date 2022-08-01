# pyqt 기초 1


import sys
# PyQt5 디렉토리에 있는 QtWidgets.py 파일의 모든 것을 불러오기
from PyQt5.QtWidgets import *

# sys.argv : sys.py 파일에 있는 list object
app = QApplication(sys.argv)

label = QLabel("Hello")
label.show()

app.exec_()


# PyQt로 만든 GUI 프로그램에 반드시 필요한 두 가지
#   1. QApplication 클래스의 instance :
#       PyQt 클래스들을 사용하기 위해서 필요하다.
#   2. Event loop :
#       사용자가 'X'버튼을 누를 때까지 GUI 프로그램 실행이 종료되지 않게 만들어 주는 loop
#       event loop가 없으면 사용자가 'X'버튼을 누르기 전에 GUI 프로그램 실행이 종료된다.
#       QApplication.exec_()가 event loop를 만들어 준다.

# PyQt 코드 구성
#    1. QApplication의 instance 생성
#    2. GUI 윈도우를 구성하는 코드 작성
#    3. event loop 생성