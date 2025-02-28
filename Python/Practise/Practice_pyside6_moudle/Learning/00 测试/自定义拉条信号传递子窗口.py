from PySide6.QtCore import Qt, QSize, Signal
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QSlider

class MyWindow(QWidget):
    sendSliderValueToSubWindow = Signal(int)
    def __init__(self):
        super().__init__()
        self.setWindowTitle(u'主窗口')
        self.resize(250, 80)

        self.mainLayout = QVBoxLayout(self)
        self.setLayout(self.mainLayout)

        self.lb = QLabel(self)
        self.slider = QSlider(Qt.Orientation.Horizontal, self)
        self.slider.setRange(0, 100)
        self.slider.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.slider.setTickInterval(10)

        self.mainLayout.addWidget(self.lb)
        self.mainLayout.addWidget(self.slider)

        self.bind()
    
    def bind(self):
        self.subWindow = SubWindow()
        self.subWindow.show()

        self.sendSliderValueToSubWindow.connect(self.subWindow.lb.setNum)
        self.slider.valueChanged.connect(lambda: self.lb.setNum(self.slider.value()))
        self.slider.valueChanged.connect(self.sendSignal)

    def sendSignal(self):
        self.sendSliderValueToSubWindow.emit(self.slider.value())

class SubWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(u'子窗口')
        self.resize(250, 80)
        
        self.mainLayout = QVBoxLayout(self)
        self.setLayout(self.mainLayout)

        self.lb = QLabel(self)
        
        self.mainLayout.addWidget(self.lb)

if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()