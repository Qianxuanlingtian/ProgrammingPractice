from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        mainLayout = QVBoxLayout()
        horiLayout1 = QHBoxLayout()
        horiLayout2 = QHBoxLayout()
        horiLayout3 = QHBoxLayout()

        button1 = QPushButton('按钮')
        button1.clicked.connect(self.hello)
        button2 = QPushButton('你好')
        button2.clicked.connect(self.hello)
        button3 = QPushButton('测试')
        button3.clicked.connect(self.hello)
        button4 = QPushButton('按钮')
        button4.clicked.connect(self.hello)
        button5 = QPushButton('你好')
        button5.clicked.connect(self.hello)
        button6 = QPushButton('测试')
        button6.clicked.connect(self.hello)
        button7 = QPushButton('按钮')
        button7.clicked.connect(self.hello)
        button8 = QPushButton('你好')
        button8.clicked.connect(self.hello)
        button9 = QPushButton('测试')
        button9.clicked.connect(self.hello)

        mainLayout.addLayout(horiLayout1)
        horiLayout1.addWidget(button1)
        horiLayout1.addWidget(button2)
        horiLayout1.addWidget(button3)

        mainLayout.addLayout(horiLayout2)
        horiLayout2.addWidget(button4)
        horiLayout2.addWidget(button5)
        horiLayout2.addWidget(button6)

        mainLayout.addLayout(horiLayout3)
        horiLayout3.addWidget(button7)
        horiLayout3.addWidget(button8)
        horiLayout3.addWidget(button9)

        self.setLayout(mainLayout)

    def hello(self):
        print('hello world')

if __name__ == "__main__":
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()