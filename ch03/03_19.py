# # pyqt 윈도우 꾸미기 5

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 300, 300)
        self.setWindowTitle("PyQt")
        self.setWindowIcon(QIcon("saturn.png"))

        btn = QPushButton("버튼", self)

        btn.clicked.connect(self.btn_clicked)

    # 콜백함수 : 이벤트 루프가 호출하는 메서드
    def btn_clicked(self):
        # window가 아니라 console에 출력
        print("btn이 클릭 되었다")

app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()

# 버튼이 정상적으로 생성 되었다.
# 하지만 버튼을 클릭해도 아무런 변화가 없다.
# 버튼에 클릭 이벤트를 추가하면 버튼을 클릭했을 때 어떤 변화가 생기게 만들 수 있다.

# 'clicked' 이벤트
#   - 사용자가 클릭하면 발생하는 이벤트
#   - widget별로 다양한 이벤트가 있다

# 어떤 widget에 clicked 이벤트가 발생할 떄 어떤 메서드가 호출 되게 하려면 이벤트와 메서드를 연결해야 한다.
# 따라서 사용자가 버튼을 클릭했을 때, 어떤 메서드가 호출 되게 하려면 클릭 이벤트와 호출할 메서드를 연결해야 한다.

# QPushButton.clicked.connect(메서드)
#   - QPushButton의 instance에 clicked 이벤트가 발생했을 때, 특정 메서드를 연결해서 호출하는 방법
#   - event loop가 발생한 event에 connect된 메서드를 호출해준다.
#   - 여기서 호출되는 메서드를 콜백함수라고 부른다.
