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
- 03_20.py : Qt Designer로 UI 제작 및 불러오기, QtDesigner, uic.loadUiType, setupUi()
- 03_21.py : Qt Designer로 생성한 widget의 이벤트 처리, 객체 탐색기 object name 확인하는 방법
- 03_22.py : 시세 조회기의 조회 버튼 이벤트 처리: inquiry 메서드 연결
- 03_23.py : 시세 조회기의 inquiry 메서드 수정 1 : 현재 가격을 console에 출력
- 03_24.py : 시제 조회기의 inquiry 메서드 수정 2 : 현재 가격 QLineEdit 위젯에 출력, QLineEdit.setText()
- 03_25.py : statusBar에 현재 시간을 1초 간격으로 출력하는 프로그램, QTimer.start(interval), QTimer.timeout.connect(method)
- 03_26.py : lineEdit에 현재 가격을 1초 간력으로 출력하는 프로그램 (시세 조회기)


# PyQt 시그널 슬롯(https://wikidocs.net/21876)
- 03_27.py : pyqtSignal, pyqtSignal.emit(), slot을 직접 정의한 signal에 연결
- 03_28.py : pyqtSignal.emit(int, int), 사용자 정의 signal로 데이터 보내기



# 참고한 자료
   - https://wikidocs.net/21873
   - https://wikidocs.net/21874
   - https://wikidocs.net/21875
   - https://wikidocs.net/21876


# 참고할 자료
   - https://github.com/pyqt/examples
   - https://opentutorials.org/module/544/4998
   - https://www.riverbankcomputing.com/static/Docs/PyQt5/
   - https://www.pythonguis.com/pyqt5-tutorial/






# PyQt로 UI 구성하는 방법
   - 방법 1 : Qt Designer 사용 (uic 모듈의 loadUiType()이 instance로 만듦)
   - 방법 2 : 코드로 instance 생성


# draft
   - Class Name : Calculator
   - Member Variables :
       - n-Operators? : int = 0
       - ???
   - Methods :
       - add
       - multiply
       - subtract
       - divide
       - ???
