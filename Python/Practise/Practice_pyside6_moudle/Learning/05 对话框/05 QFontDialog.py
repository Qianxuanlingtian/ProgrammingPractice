from PySide6.QtCore import Qt, QSize
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFontDialog, QTextEdit

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.mainLayout = QVBoxLayout(self)
        self.setLayout(self.mainLayout)
        
        self.textEdit = QTextEdit(self)
        self.btn = QPushButton(u'点我更改字体', self)
        self.btn.clicked.connect(self.changeFont)

        self.mainLayout.addWidget(self.textEdit)
        self.mainLayout.addWidget(self.btn)

    def changeFont(self) -> None:
        ok, font = QFontDialog.getFont(self)
        if not ok: return
        self.textEdit.setFont(font)

if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()