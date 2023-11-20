import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter,  QColor
from random import randint

class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.initUI()

    def initUI(self):
        self.pushButton.clicked.connect(self.paint)
        self.do_paint = False

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_fn(qp)
            qp.end()
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()

    def draw_fn(self, qp):
        a = randint(30, 200)
        r, g, b = 255, 255, 0
        qp.setBrush(QColor(r, g, b))
        qp.drawEllipse(300 - a // 2, 400 - a // 2, a, a)
        qp.setBrush(QColor(r, g, b))
        qp.drawEllipse(500 - a // 2, 200 - a // 2, a, a)
        qp.setBrush(QColor(r, g, b))
        qp.drawEllipse(420 - a // 2, 300 - a // 2, a, a)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())