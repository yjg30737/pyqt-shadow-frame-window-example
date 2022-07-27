from PyQt5.QtCore import Qt, QRectF, QMargins
from PyQt5.QtGui import QColor, QPainter, QPainterPath, QBrush, QPen, QRegion, QPalette
from PyQt5.QtWidgets import QWidget, QMainWindow, QApplication, QGraphicsDropShadowEffect, QGridLayout, QLabel, \
    QTextEdit, QVBoxLayout


# shadow + rounded frame
class ShadowFrame(QWidget):
    def __init__(self, main_window):
        super().__init__()
        # main_window is main widget to show
        self.__main_window = main_window
        self.__initUi()

    def __initUi(self):
        # for frameless window/prevent occurrence of minor bugs
        self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint | Qt.WindowMinMaxButtonsHint)
        # make basic background(which is dark) invisible to show shadow
        self.setAttribute(Qt.WA_TranslucentBackground)

        # set the shadow
        self.__effect = QGraphicsDropShadowEffect()
        self.__effect.setBlurRadius(12.0)
        self.__effect.setColor(QColor(0, 0, 0, 127))
        self.__effect.setOffset(0.0)
        self.setGraphicsEffect(self.__effect)

        lay = QGridLayout()
        lay.addWidget(self.__main_window)
        self.setLayout(lay)

    def paintEvent(self, e):
        painter = QPainter(self)
        # set the background and pen (looks like Windows 11 default window)
        pen = QPen(QColor(Qt.gray), 1)
        brush = QBrush(QColor(241, 241, 241, 255))
        painter.setPen(pen)
        painter.setBrush(brush)

        # set rounded window
        path = QPainterPath()
        rect = self.rect()
        # set margin to each direction for giving the space to show shadow
        rect = rect.marginsRemoved(QMargins(5, 5, 5, 5))
        # rounded corner's radius
        radius = 12.0
        path.addRoundedRect(QRectF(rect), radius, radius)
        # set antialiasing to enhance quality of window
        painter.setRenderHints(QPainter.Antialiasing)
        painter.drawPath(path)

        return super().paintEvent(e)


# sample widget to put inside the shadow(+rounded) frame
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
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
    # put inside the shadow(+rounded) frame
    window = ShadowFrame(widget)
    window.show()
    app.exec_()
