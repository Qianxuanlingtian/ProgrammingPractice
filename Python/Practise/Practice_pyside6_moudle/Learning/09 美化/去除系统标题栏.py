from PySide6.QtWidgets import (QApplication, QWidget, QStyle, QVBoxLayout, QPushButton,
                               QLabel, QHBoxLayout, 
                               QGridLayout, QLineEdit, QSpinBox, QSlider, QComboBox)
from PySide6.QtCore import QSize, Qt

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        # 删除窗体系统标题栏
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        
        # 自定义标题栏
        self.titleLabel = QLabel(u"自定义标题栏")
        self.minimizeButton = QPushButton(u'最小化')
        self.closeButton = QPushButton(u'关闭')

        self.minimizeButton.clicked.connect(lambda: self.showMinimized())
        self.closeButton.clicked.connect(lambda: self.close())

        self.titleLayout = QHBoxLayout()
        self.titleLayout.addWidget(self.titleLabel)
        self.titleLayout.addWidget(self.minimizeButton)
        self.titleLayout.addWidget(self.closeButton)
        
        self.setFixedSize(QSize(400, 300))

        self.mainLayout = QVBoxLayout()
        self.setLayout(self.mainLayout)

        self.lineEdit = QLineEdit(self)
        self.button = QPushButton('按钮', self)
        self.spinBox = QSpinBox()
        self.slider = QSlider(Qt.Orientation.Horizontal, self)
        self.comboBox = QComboBox(self)

        self.mainLayout.addLayout(self.titleLayout)
        self.mainLayout.addWidget(self.lineEdit)
        self.mainLayout.addWidget(self.button)
        self.mainLayout.addWidget(self.spinBox)
        self.mainLayout.addWidget(self.slider)
        self.mainLayout.addWidget(self.comboBox)

if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()