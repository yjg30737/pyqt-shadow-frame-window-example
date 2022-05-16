# pyqt-shadow-frame-window-example
PyQt shadow frame window example

Show the slight shadow around the window's border.

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
    app.exec_()
```

Result

![image](https://user-images.githubusercontent.com/55078043/168698986-50a046fa-2467-4195-9776-c4eee6ac9d48.png)

