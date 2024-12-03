from PyQt6.QtWidgets import QApplication
from interface import form


import sys


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = form()
    ex.show()
    sys.exit(app.exec())
