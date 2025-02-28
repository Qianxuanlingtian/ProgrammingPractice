from PIL import Image, ImageFilter, ImageQt
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QSlider, QLabel

class MyWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setObjectName('dialogTestForm')
        self.setWindowTitle(u'图像模糊处理示例项目')
        self.resize(QSize(400, 300))

        self.mainLayout = QVBoxLayout(self)

        self.btn = QPushButton(u'点我打开图像文件', self)
        self.btn.clicked.connect(self.openImageDialog)
        self.imageLabel = QLabel(self)
        self.controlSlider = QSlider(Qt.Orientation.Horizontal, self, tickPosition=QSlider.TickPosition.TicksBelow, tickInterval=2)
        self.controlSlider.setRange(0, 20)
        self.controlSlider.valueChanged.connect(self.imageProcess)

        self.mainLayout.addWidget(self.btn)
        self.mainLayout.addWidget(self.imageLabel)
        self.mainLayout.addWidget(self.controlSlider)

        self.setLayout(self.mainLayout)

    def openImageDialog(self) -> None:
        self.image = Image.open(QFileDialog.getOpenFileName(self, '选择图像', './', '图像文件(*.jpg *.png *.bmp)')[0])
        self.imageLabel.setPixmap(ImageQt.toqpixmap(self.image))

    def imageProcess(self, value) -> None:
        self.blurPic = self.image.filter(ImageFilter.GaussianBlur(value))
        self.imageLabel.setPixmap(ImageQt.toqpixmap(self.blurPic))

if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()