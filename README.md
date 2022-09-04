# pyqt-shadow-frame-window-example
PyQt shadow(+rounded) frame window example.

You can move and resize this.

Show the slight shadow around the window's border.

== 2022-07-27 ==

From v0.0.2, window's edges are rounded.

Should've changed the name as pyqt-shadow-rounded-frame-window or something but i'm kinda lazy so whatever.

== 2022-08-06 ==

From v0.0.3, window can be resized and moved by inheriting FramelessWindow in <a href="https://github.com/yjg30737/pyqt-frameless-window.git">pyqt-frameless-window</a>.

== 2022-09-04 ==

From v0.0.31(don't care about the version policy, just want to slow down), window's shadow and border disappear when window is full screen or maximized. They will reappear when window is back to normal.

## Requirements
* PyQt5 >= 5.15

## Setup
`python -m pip install git+https://github.com/yjg30737/pyqt-shadow-frame-window-example.git --upgrade`

## Included Package
* <a href="https://github.com/yjg30737/pyqt-frameless-window.git">pyqt-frameless-window</a>

## Example
Code Sample
```python
from PyQt5.QtWidgets import QApplication
from pyqt_shadow_frame_window_example import MainWindow, ShadowFrame

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    widget = MainWindow()
    window = ShadowFrame(widget)
    window.show()
    app.exec()
```

Result

![image](https://user-images.githubusercontent.com/55078043/181148746-f65b0b34-8aed-443f-bf15-c1604d450dc1.png)

Inspired by Windows 11 GUI.
