import os
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PySide6.QtGui import QPixmap
import source_rc

os.chdir(os.path.dirname(os.path.abspath(__file__)))

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.mainLayout = QVBoxLayout(self)
        self.setLayout(self.mainLayout)

        self.lb = QLabel(self)
        self.lb.setPixmap(QPixmap(':/images/test.png'))
        # self.lb.setScaledContents(True)

        self.mainLayout.addWidget(self.lb)

if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()