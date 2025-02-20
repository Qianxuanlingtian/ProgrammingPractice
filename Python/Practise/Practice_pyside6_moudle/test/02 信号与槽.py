from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        mainLayout = QVBoxLayout()

        button = QPushButton('按钮')
        button.clicked.connect(self.hello)

        mainLayout.addWidget(button)
        self.setLayout(mainLayout)

    def hello(self):
        print('hello world')

if __name__ == "__main__":
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()