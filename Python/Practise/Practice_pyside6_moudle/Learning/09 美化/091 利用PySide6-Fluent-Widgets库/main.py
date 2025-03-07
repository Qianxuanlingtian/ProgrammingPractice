from typing import Any
from PySide6.QtCore import Qt, QSize
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QFrame
from qfluentwidgets import (FluentWindow, VBoxLayout, FlowLayout, ExpandLayout, 
                            ProgressBar, FluentIconBase, FluentIcon,
                            NavigationItemPosition, SubtitleLabel, setFont)

class Widget(QFrame):
    def __init__(self, text:str, parent:Any = None):
        super().__init__(parent=parent)
        self.setObjectName(text+'FrameWidget')
        self.label = SubtitleLabel()

class MyWindow(FluentWindow):
    def __init__(self):
        super().__init__()
        self.resize(QSize(400, 300))
        self.homeWidget = Widget('home')

        self.addSubInterface(interface=self.homeWidget, icon=FluentIcon.HOME, text='主页', position=NavigationItemPosition.TOP)



if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()