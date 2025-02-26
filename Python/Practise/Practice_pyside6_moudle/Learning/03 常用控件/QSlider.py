from PySide6.QtCore import Qt, QSize
from PySide6.QtWidgets import QApplication, QWidget, QSlider, QVBoxLayout, QGridLayout

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        if not self.objectName():
            self.setObjectName(u'test')
        self.resize(QSize(600, 400))
        self.setWindowTitle(u'拉条组测试')

        self.mainLayout = QVBoxLayout()

        self.horiSlider = QSlider(Qt.Orientation.Horizontal, self)
        self.horiSlider.setTickPosition(QSlider.TickPosition.TicksBothSides)
        self.horiSlider.setTickInterval(1)
        self.vertSlider = QSlider(Qt.Orientation.Vertical, self)
        self.vertSlider.setTickPosition(QSlider.TickPosition.TicksBothSides)
        self.vertSlider.setTickInterval(2)

        self.mainLayout.addWidget(self.horiSlider)
        self.mainLayout.addWidget(self.vertSlider)

        self.setLayout(self.mainLayout)

        self.horiSlider.valueChanged.connect(lambda: print(f'self.horiSlider.value = {self.horiSlider.value()}'))
        self.horiSlider.valueChanged.connect(self.change)
        self.vertSlider.valueChanged.connect(lambda: print(f'self.vertSlider.value = {self.vertSlider.value()}'))

    def change(self):
        value = self.horiSlider.value()
        self.vertSlider.setValue(value)

    def func(self):
        # sender()
        pass

if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()