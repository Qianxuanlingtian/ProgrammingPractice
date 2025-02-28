from PySide6.QtCore import Qt, QSize
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(u'主窗口')

        self.mainLayout = QVBoxLayout(self)
        self.setLayout(self.mainLayout)

        self.subWindow = SubWindow()

        self.lb = QLabel(u'这是一个主窗口')
        self.btnOpenSubWindow = QPushButton(u'打开子窗口', self)
        self.btnOpenSubWindow.clicked.connect(lambda: self.subWindow.show())
        self.btnHideSubWindow = QPushButton(u'隐藏子窗口', self)
        self.btnHideSubWindow.clicked.connect(lambda: self.subWindow.hide())
        self.btnCloseSubWindow = QPushButton(u'关闭子窗口', self)
        self.btnCloseSubWindow.clicked.connect(lambda: self.subWindow.close())

        self.mainLayout.addWidget(self.lb)
        self.mainLayout.addWidget(self.btnOpenSubWindow)
        self.mainLayout.addWidget(self.btnHideSubWindow)
        self.mainLayout.addWidget(self.btnCloseSubWindow)


class SubWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(u'子窗口')
        
        self.mainLayout = QVBoxLayout(self)
        self.setLayout(self.mainLayout)

        self.lb = QLabel(u'这是一个子窗口的示例')
        self.lineEdit = QLineEdit(self)
        self.lineEdit.setText(u'这是子窗口的文本框')

        self.mainLayout.addWidget(self.lb)
        self.mainLayout.addWidget(self.lineEdit)

if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()