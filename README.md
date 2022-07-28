# 목표 : GUI 계산기 구현 by PyQt

# PyQt
    Python GUI(Graphical User Interface) 모듈
    TUI(Text-based User Interface) 모듈이 아니다.

# PyQt5 기초(https://wikidocs.net/21873)
- 03_11.py : python 객체 복습
- 03_12.py : QApplication, QLabel, QApplication.exec_()
- 03_13.py : QPushButton
- 03_14.py : QMainWindow

# PyQt5 윈도우 꾸미기(https://wikidocs.net/21874)
- 03_15.py : QMainWindow.setGeometry(ax, ay, aw, ah)
- 03_16.py : QMainWindow.setTitle(title), QIcon, QMainWindow.setWindowIcon(QIcon(path))
- 03_17.py : constructor에 QPushButton 추가
- 03_18.py : 버튼 두개 추가, QPushButton.move(ax, ay)
- 03_19.py : 버튼에 클릭 이벤트 추가, QPushButton.clicked.connect(method)

# PyQt Qt Designer(https://wikidocs.net/21875)
- 03_20.py : QtDesigner(C:/Users/USER/anaconda3/Library/bin/designer.exe), uic.loadUiType, setupUi()
- 03_21.py : qt designer로 추가한 버튼에 클릭 이벤트 메서드(btn_clicked) 연결
- 03_22.py : qt designer로 추가한 버튼에 클릭 이벤트 메서드(inquiry) 연결
- 03_23.py : qt designer로 추가한 버튼을 클릭 이벤트 메서드(inquiry : 비트코인 현재가를 콘솔에 출력) 연결
- 03_24.py : qt designer로 추가한 버튼을 클릭 이벤트 메서드(inquiry : QLineEdit 위젯에 출력) 연결
- 03_25.py : QTimer, QTimer.start(), QTimer.timeout.connect()
- 03_26.py :
- 03_27.py :



# 참고한 자료
   - https://wikidocs.net/21873
   - https://wikidocs.net/21874
   - https://wikidocs.net/21875


# 참고할 자료
   - MS Window10 계산기
   - https://github.com/pyqt/examples
   - https://wikidocs.net/21876





# PyQt로 UI 구성하는 방법
   - 방법 1 : Qt Designer 사용 (uic 모듈의 loadUiType()이 instance로 만듦)
   - 방법 2 : 코드로 instance 생성


# draft
   - Class Name : Calculator
   - Member Variables :
       - n-Operators? : int = 0.0
       - ???
   - Methods :
       - add
       - multiply
       - subtract
       - divide
       - ???
