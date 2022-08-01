from PyQt5.QtCore import QDate, QTime, QDateTime

now = QDate.currentDate()
time = QTime.currentTime()
datetime = QDateTime.currentDateTime()
print(now.toString())
print(time.toString())
print(datetime.toString())