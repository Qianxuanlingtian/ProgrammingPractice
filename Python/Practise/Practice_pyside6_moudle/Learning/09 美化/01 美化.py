from PySide6.QtWidgets import QApplication, QWidget, QStyle, QVBoxLayout, QPushButton, QGridLayout, QLineEdit, QSpinBox, QSlider, QComboBox
from PySide6.QtCore import QSize, Qt

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(QSize(400, 300))

        self.mainLayout = QVBoxLayout()
        self.setLayout(self.mainLayout)

        self.lineEdit = QLineEdit(self)
        self.button = QPushButton('按钮', self)
        self.spinBox = QSpinBox(self)
        self.slider = QSlider(Qt.Orientation.Horizontal, self)
        self.comboBox = QComboBox(self)

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