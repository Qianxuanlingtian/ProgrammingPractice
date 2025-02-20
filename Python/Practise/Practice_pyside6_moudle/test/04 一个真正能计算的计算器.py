from PySide6.QtWidgets import QApplication, QWidget, QLineEdit, QVBoxLayout, QPushButton
from Ui_calculator import Ui_Form

class Calculator(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication([])
    window = Calculator()
    window.show()
    app.exec()