from PySide6.QtCore import QSize
from PySide6.QtWidgets import QApplication, QWidget
from qfluentwidgets import (FluentWindow,
                            FluentIconBase,
                            FluentIcon,
                            FlowLayout,
                            PushButton)

class MyWindow(FluentWindow):
    def __init__(self):
        super().__init__()
        self.homeWidget = QWidget()
        self.homeWidget.setObjectName('HomepageWidget')

        self.homeLayout = FlowLayout(self.homeWidget)
        self.homeLayout.addWidget(PushButton('测试'))

        self.addSubInterface(self.homeWidget, FluentIcon.HOME, "主页")

if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()