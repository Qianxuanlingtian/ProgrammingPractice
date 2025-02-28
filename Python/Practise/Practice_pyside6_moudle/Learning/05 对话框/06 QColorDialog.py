from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QColorDialog, QTextEdit

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.mainLayout = QVBoxLayout(self)
        self.setLayout(self.mainLayout)
        
        self.textEdit = QTextEdit(self)
        self.textEdit.setFont(QFont(u'微软雅黑', 36))
        self.btn = QPushButton(u'点我更改字体颜色', self)
        self.btn.clicked.connect(self.changeColor)

        self.mainLayout.addWidget(self.textEdit)
        self.mainLayout.addWidget(self.btn)

    def changeColor(self) -> None:
        fontColor = QColorDialog.getColor()
        self.textEdit.setTextColor(fontColor)

if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()