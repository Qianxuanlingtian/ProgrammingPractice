from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QStyle, QSpinBox

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.mainLayout = QVBoxLayout(self)
        self.setLayout(self.mainLayout)

        self.lb = QLabel()
        self.lb.setPixmap(self.style().standardPixmap(QStyle.StandardPixmap.SP_ComputerIcon))

        self.spinBox = QSpinBox(self)

        self.mainLayout.addWidget(self.spinBox)
        self.mainLayout.addWidget(self.lb)

if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()