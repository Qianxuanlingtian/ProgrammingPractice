from PySide6.QtCore import Qt, QSize
from PySide6.QtWidgets import QApplication, QWidget, QSlider, QVBoxLayout

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        if not self.objectName():
            self.setObjectName(u'拉条组件测试')
        # self.resize(QSize(600, 400))

        self.horiSlider = QSlider(self)
        self.horiSlider.setOrientation(Qt.Orientation.Horizontal)

        self.vertSlider = QSlider(self)
        self.vertSlider.setOrientation(Qt.Orientation.Vertical)

        self.mainLayout = QVBoxLayout(self)
        self.mainLayout.addWidget(self.horiSlider)
        self.mainLayout.addWidget(self.vertSlider)

        self.setLayout(self.mainLayout)


if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()