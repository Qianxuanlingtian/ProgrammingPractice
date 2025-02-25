from PySide6.QtWidgets import QApplication, QWidget
from Ui_calculator import Ui_Form

class Calculator(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.result = ''
        self.bind()
    
    def bind(self):
        self.pushButton_0.clicked.connect(lambda: self.addElement('0'))
        self.pushButton_1.clicked.connect(lambda: self.addElement('1'))
        self.pushButton_2.clicked.connect(lambda: self.addElement('2'))
        self.pushButton_3.clicked.connect(lambda: self.addElement('3'))
        self.pushButton_4.clicked.connect(lambda: self.addElement('4'))
        self.pushButton_5.clicked.connect(lambda: self.addElement('5'))
        self.pushButton_6.clicked.connect(lambda: self.addElement('6'))
        self.pushButton_7.clicked.connect(lambda: self.addElement('7'))
        self.pushButton_8.clicked.connect(lambda: self.addElement('8'))
        self.pushButton_9.clicked.connect(lambda: self.addElement('9'))
        self.pushButton_point.clicked.connect(lambda: self.addElement('.'))
        self.pushButton_add.clicked.connect(lambda: self.addElement('+'))
        self.pushButton_sub.clicked.connect(lambda: self.addElement('-'))
        self.pushButton_mul.clicked.connect(lambda: self.addElement('*'))
        self.pushButton_div.clicked.connect(lambda: self.addElement('/'))
        self.pushButton_equal.clicked.connect(self.calculate)
        self.pushButton_clear.clicked.connect(self.clear)
        self.pushButton_del.clicked.connect(self.delete)

    def addElement(self, param: str):
        self.lineEdit.clear()
        self.result += param
        self.lineEdit.setText(self.result)
    
    def calculate(self):
        try:
            self.result = str(eval(self.result))
            self.lineEdit.setText(self.result)
        except:
            self.lineEdit.setText('Error')
    
    def clear(self):
        self.result = ''
        self.lineEdit.clear()

    def delete(self):
        self.result = self.result[:-1]
        self.lineEdit.setText(self.result)


if __name__ == "__main__":
    app = QApplication([])
    window = Calculator()
    window.show()
    app.exec()