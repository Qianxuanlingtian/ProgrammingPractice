from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QFileDialog, QPushButton

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QFileDialogTest')

        self.mainLayout = QVBoxLayout(self)
        self.setLayout(self.mainLayout)

        self.btn1 = QPushButton('选择文件对话框', self)
        self.btn1.clicked.connect(lambda: print(QFileDialog.getOpenFileName(self, '标题', './',
                                                                            '所有文件(*);;文本文件(*.txt);;python文件(*.py *.pyi)',
                                                                            options=QFileDialog.Options())))
        self.btn2 = QPushButton('选择多个文件对话框', self)
        self.btn2.clicked.connect(lambda: print(QFileDialog.getOpenFileNames(self, '标题', './',
                                                                             '所有文件(*);;文本文件(*.txt);;python文件(*.py *.pyi)',
                                                                             options=QFileDialog.Options())))
        self.btn3 = QPushButton('选择文件夹对话框', self)
        self.btn3.clicked.connect(lambda: print(QFileDialog.getExistingDirectory(self, '标题', './',
                                                                               options=QFileDialog.Options())))
        self.btn4 = QPushButton('保存文件对话框', self)
        self.btn4.clicked.connect(lambda: print(QFileDialog.getSaveFileName(self, '标题', './',
                                                                            '所有文件(*);;文本文件(*.txt);;python文件(*.py *.pyi)',
                                                                            options=QFileDialog.Options())))

        self.mainLayout.addWidget(self.btn1)
        self.mainLayout.addWidget(self.btn2)
        self.mainLayout.addWidget(self.btn3)
        self.mainLayout.addWidget(self.btn4)
        

if __name__ == "__main__":
    app = QApplication([])
    win = MyWindow()
    win.show()
    app.exec()