from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor

import sys
from random import randint

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui.ui', self)

        self.drawing = 0
        self.create_circle_btn.clicked.connect(self.create_circle)
        self.x = self.y = self.diameter = 0

    def create_circle(self):
        self.drawing = 1
        self.repaint()

    def paintEvent(self, event):
        if self.drawing:
            self.x = randint(20, 700)
            self.y = randint(70, 600)
            self.diameter = randint(30, 250)
            self.drawing = 0

        qp = QPainter(self)
        qp.begin(self)
        qp.setBrush(QColor(252, 217, 117))
        qp.drawEllipse(self.x, self.y, self.diameter, self.diameter)
        qp.end()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
