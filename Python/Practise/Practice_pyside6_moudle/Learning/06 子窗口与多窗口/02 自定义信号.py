"""
自定义信号基本流程：
1. 定义信号
通过from PySide6.QtCore import Signal导入Signal类，然后在类中定义信号对象。
注意：信号对象必须定义在类的外部，不能在方法中定义，不能在__init__方法中定义，否则会报错。
2. 绑定信号
通过自定义信号对象的connect方法绑定信号，具体形式为：自定义信号对象.connect(需要激活的函数（槽函数）)。
2. 发送信号
通过自定义信号对象的emit方法发送信号，具体形式为：自定义信号对象.emit(参数)。
3. 接收信号
目标对象接收信号，执行槽函数。
"""

from PySide6.QtCore import Qt, QSize, Signal
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit

class MyWindow(QWidget):
    sendValueToSubWindow = Signal(str)
    def __init__(self):
        super().__init__()
        self.setWindowTitle(u'主窗口')

        self.mainLayout = QVBoxLayout(self)
        self.setLayout(self.mainLayout)

        self.lineEdit = QLineEdit(self)
        self.btn = QPushButton(u'发送信号', self)

        self.mainLayout.addWidget(self.lineEdit)
        self.mainLayout.addWidget(self.btn)

        self.bind()
    
    def bind(self):
        self.subWindow = SubWindow()
        self.subWindow.show()

        self.sendValueToSubWindow.connect(self.subWindow.lineEdit.setText)
        self.btn.clicked.connect(self.sendSignal)

    def sendSignal(self):
        self.sendValueToSubWindow.emit(self.lineEdit.text())
    

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