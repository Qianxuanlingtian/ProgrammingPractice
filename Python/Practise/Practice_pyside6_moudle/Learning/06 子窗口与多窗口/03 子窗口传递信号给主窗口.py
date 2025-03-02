from PySide6.QtCore import Qt, QSize, Signal
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(u'主窗口')

        self.mainLayout = QVBoxLayout(self)
        self.setLayout(self.mainLayout)

        self.lb = QLabel(u'这是一个主窗口')

        self.mainLayout.addWidget(self.lb)

        self.bind()
    
    def bind(self):
        self.subWindow = SubWindow(self)
        self.subWindow.show()

class SubWindow(QWidget):
    sendValueToMainWindow = Signal(str)

    def __init__(self, parent=None):
        self.parent = parent

        super().__init__()
        self.setWindowTitle(u'子窗口')
        
        self.mainLayout = QVBoxLayout(self)
        self.setLayout(self.mainLayout)

        self.lineEdit = QLineEdit(self)
        self.lineEdit.setText(u'这是子窗口的文本框')
        self.btn = QPushButton(u'发送信号给主窗口', self)
        
        self.mainLayout.addWidget(self.lineEdit)
        self.mainLayout.addWidget(self.btn)

        self.bind()
    
    def bind(self):
        self.sendValueToMainWindow.connect(self.parent.lb.setText)
        self.btn.clicked.connect(self.sendSignal)

    def sendSignal(self):
        self.sendValueToMainWindow.emit(self.lineEdit.text())


if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()