from PyQt6.QtWidgets import QWidget, QApplication
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import QPointF

from random import randint

from PyQt6 import uic

import sys


class form(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI.ui", self)

        self.button.clicked.connect(self.click)
        self.color = QColor(255, 255, 0)

        self.flag = 0

    def paintEvent(self, event):
        if not self.flag:
            return

        qp = QPainter()
        qp.begin(self)

        self.krugi(qp)

        qp.end()

    def krugi(self, qp):
        qp.setBrush(self.color)

        self.size_1 = randint(10, 100)
        self.size_2 = randint(10, 100)

        qp.drawEllipse(QPointF(150, 200), self.size_1, self.size_1)
        qp.drawEllipse(QPointF(500, 200), self.size_2, self.size_2)

    def click(self):
        self.flag = 1
        self.update()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = form()
    ex.show()
    sys.exit(app.exec())
