import sys
from PyQt5.QtWidgets import *
# with open('demo.qss','r') as f:
#     qApp.setStyleSheet(f.read())

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        with open('demo.qss', 'r') as f:
            qApp.setStyleSheet(f.read())
        self.setWindowTitle('demo')
        self.resize(500,500)
        label=QLabel(self)
        label.setText('社会我顺哥')
        label1 = QLabel(self)
        label1.setText('社会我顺哥')
        label1.setObjectName('notice')
        label1.setProperty('notice_level','warning')
        label1.move(100,100)
        # label.setStyleSheet('font-size:20px;color:red;')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())