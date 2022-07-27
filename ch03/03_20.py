from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("mywindow.ui")[0]


class Mywindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


app = QApplication([])
window = Mywindow()
window.show()
app.exec_()


