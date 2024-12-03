from PyQt6.QtWidgets import QWidget, QApplication, QPushButton
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import QPointF

from random import randint

import sys


class form(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

        self.button.clicked.connect(self.click)

        self.flag = 0

    def initUi(self):
        self.setGeometry(300, 300, 500, 500)

        self.button = QPushButton("жмак", self)
        self.button.resize(200, 140)
        self.button.move(150, 350)

    def paintEvent(self, event):
        if not self.flag:
            return

        qp = QPainter()
        qp.begin(self)

        self.krugi(qp)

        qp.end()

    def krugi(self, qp):
        self.size_1 = randint(10, 100)
        self.size_2 = randint(10, 100)

        self.color1 = QColor(randint(0, 255), randint(0, 255), randint(0, 255))
        self.color2 = QColor(randint(0, 255), randint(0, 255), randint(0, 255))

        qp.setBrush(self.color1)
        qp.drawEllipse(QPointF(120, 200), self.size_1, self.size_1)

        qp.setBrush(self.color2)
        qp.drawEllipse(QPointF(350, 200), self.size_2, self.size_2)

    def click(self):
        self.flag = 1
        self.update()