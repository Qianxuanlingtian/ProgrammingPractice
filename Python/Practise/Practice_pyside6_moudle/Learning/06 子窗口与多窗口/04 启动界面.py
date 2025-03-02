from PySide6.QtCore import Qt, QSize, Signal, QTimer
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel

class LoadingWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(u'加载窗口')
        self.resize(200, 100)

        self.mainLayout = QVBoxLayout(self)
        self.setLayout(self.mainLayout)

        self.lb = QLabel(u'加载中...', self)
        self.lb.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.mainLayout.addWidget(self.lb)

        self.timer = QTimer(self)
        self.timer.singleShot(3000, self.openMainWindow)

    def openMainWindow(self):
        self.mainWindow = MyWindow()
        self.mainWindow.show()
        self.close()


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(u'主窗口')

        self.mainLayout = QVBoxLayout(self)
        self.setLayout(self.mainLayout)

        self.lb = QLabel(u'这是一个主窗口', self)

        self.mainLayout.addWidget(self.lb)

if __name__ == '__main__':
    app = QApplication([])
    window = LoadingWindow()
    window.show()
    app.exec()