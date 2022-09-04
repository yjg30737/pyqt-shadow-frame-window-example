from PyQt5.QtCore import Qt, QRectF, QMargins
from PyQt5.QtGui import QColor, QPainter, QPainterPath, QBrush, QPen
from PyQt5.QtWidgets import QWidget, QMainWindow, QApplication, QGraphicsDropShadowEffect, QGridLayout, QLabel, \
    QTextEdit, QVBoxLayout
from pyqt_frameless_window import FramelessWindow


# shadow + rounded frame
# inherits FramelessWindow for resizing and moving feature
class ShadowFrame(FramelessWindow):
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

        lay = QGridLayout()
        lay.addWidget(self.__main_window)
        self.setLayout(lay)

        # make it able to move
        self.setPressToMove(True)

    def paintEvent(self, e):
        painter = QPainter(self)
        # set the background and pen (looks like Windows 11 default window)
        pen = QPen(QColor(Qt.gray), self.__borderWidth)
        brush = QBrush(QColor(241, 241, 241, 255))
        painter.setPen(pen)
        painter.setBrush(brush)

        # set rounded window
        path = QPainterPath()
        rect = self.rect()
        # set margin to each direction for giving the space to show shadow
        rect = rect.marginsRemoved(QMargins(self.__shadowMargin, self.__shadowMargin,
                                            self.__shadowMargin, self.__shadowMargin))
        # rounded corner's radius
        path.addRoundedRect(QRectF(rect), self.__borderRadius, self.__borderRadius)
        # set antialiasing to enhance quality of window
        painter.setRenderHints(QPainter.Antialiasing)
        painter.drawPath(path)

        return super().paintEvent(e)

    def event(self, e):
        if e.type() == 105:
            windowState = int(self.windowState())
            self.toggleShadowBorder(not (windowState == 2 or windowState == 4))
        return super().event(e)

    def toggleShadowBorder(self, f: bool):
        if f:
            self.__shadowBlurRadius = 6.0
            self.__borderWidth = 1
            self.__shadowMargin = self._margin
            self.__borderRadius = 12.0
        else:
            self.__shadowBlurRadius = 0
            self.__borderWidth = 0
            self.__shadowMargin = 0
            self.__borderRadius = 0

        # set the shadow
        self.__effect = QGraphicsDropShadowEffect()
        self.__effect.setBlurRadius(self.__shadowBlurRadius)
        self.__effect.setColor(QColor(0, 0, 0, 127))
        self.__effect.setOffset(0.0)
        self.setGraphicsEffect(self.__effect)

        self.repaint()


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
