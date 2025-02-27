from PySide6.QtCore import Qt, QSize
from PySide6.QtWidgets import QApplication, QWidget, QInputDialog, QVBoxLayout, QPushButton,QLineEdit

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QDialogTest')

        self.mainLayout = QVBoxLayout(self)
        self.setLayout(self.mainLayout)

        self.btn1 = QPushButton('获取一个整型数字', self)
        self.btn1.clicked.connect(self.showDialog)
        self.btn2 = QPushButton('获取一个浮点型数字', self)
        self.btn2.clicked.connect(lambda: print(QInputDialog.getDouble(self, '标题', '内容', value=1.0, minValue=0.0,
                                                                       maxValue=100.0, decimals=2, flags=Qt.Dialog)))
        self.btn3 = QPushButton('获取一个选项', self)
        self.btn3.clicked.connect(lambda: print(QInputDialog.getItem(self, '标题', '内容', ['选项1', '选项2', '选项3'],
                                                                     0, False, flags=Qt.Dialog)))
        self.btn4 = QPushButton('获取一个单行文本', self)
        self.btn4.clicked.connect(lambda: print(QInputDialog.getText(self, '标题', '内容', QLineEdit.EchoMode.NoEcho,
                                                                     text='默认值', flags=Qt.Dialog)))
        self.btn5 = QPushButton('获取一个多行文本', self)
        self.btn5.clicked.connect(lambda: print(QInputDialog.getMultiLineText(self, '标题', '内容', '默认值', flags=Qt.Dialog)))

        self.mainLayout.addWidget(self.btn1)
        self.mainLayout.addWidget(self.btn2)
        self.mainLayout.addWidget(self.btn3)
        self.mainLayout.addWidget(self.btn4)
        self.mainLayout.addWidget(self.btn5)

    def showDialog(self):
        replay = QInputDialog.getInt(self, '标题', '内容', value=1, minValue=0, maxValue=100, step=1, flags=Qt.Dialog)
        print(replay)

if __name__ == "__main__":
    app = QApplication([])
    win = MyWindow()
    win.show()
    app.exec()