from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QWidget, QMainWindow, QApplication, QGraphicsDropShadowEffect, QGridLayout, QLabel, \
    QTextEdit, QVBoxLayout


class ShadowFrame(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.__main_window = main_window
        self.__initUi()

    def __initUi(self):
        self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint | Qt.WindowMinMaxButtonsHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)

        self.__effect = QGraphicsDropShadowEffect()
        self.__effect.setBlurRadius(8.0)
        self.__effect.setColor(QColor(0, 0, 0, 127))
        self.__effect.setOffset(0.0)
        self.__main_window.setGraphicsEffect(self.__effect)

        lay = QGridLayout()
        lay.addWidget(self.__main_window)
        lay.setContentsMargins(2, 2, 2, 2)
        self.setLayout(lay)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        self.setAutoFillBackground(True)

        lbl = QLabel()
        lbl.setText('Shadow window example')
        textEdit = QTextEdit()

        lay = QVBoxLayout()
        lay.addWidget(lbl)
        lay.addWidget(textEdit)

        mainWidget = QWidget()
        mainWidget.setLayout(lay)
        self.setCentralWidget(mainWidget)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    widget = MainWindow()
    window = ShadowFrame(widget)
    window.show()
    app.exec_()
