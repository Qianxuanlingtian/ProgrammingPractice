from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QApplication, QWidget, QStyle, QVBoxLayout, QListWidget, QListWidgetItem

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.mainLayout = QVBoxLayout(self)
        self.setLayout(self.mainLayout)

        self.listWidget = QListWidget(self)
        self.listWidget.addItem(QListWidgetItem(u'测试'))
        self.listWidget.addItems([str(i) for i in range(20)])
        self.listWidget.insertItem(2, '你好')
        self.listWidget.item(4).setText('更改')
        self.listWidget.takeItem(5)

        self.mainLayout.addWidget(self.listWidget)

if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()