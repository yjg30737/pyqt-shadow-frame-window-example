# pyqt-shadow-frame-window-example
PyQt shadow(+rounded) frame window example

Show the slight shadow around the window's border.

== 2022-07-27 ==

From v0.0.2, window's edges are rounded.

Should've changed the name as pyqt-shadow-rounded-frame-window or something but i'm kinda lazy so whatever.

## Requirements
* PyQt5 >= 5.8

## Setup
`python -m pip install git+https://github.com/yjg30737/pyqt-shadow-frame-window-example.git --upgrade`

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
