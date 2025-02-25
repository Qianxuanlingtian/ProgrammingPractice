from PySide6.QtWidgets import QApplication, QWidget
from Ui_trans import Ui_Form

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.lengthVar = {'厘米': 1, '分米': 10, '米': 100, '千米': 100000}
        self.weightVar = {'克': 1, '斤': 500, '千克': 1000}
        self.TypeDict = {'长度': self.lengthVar, '重量': self.weightVar}

        self.bind()

    def bind(self):
        self.ui.dataTypeComboBox.addItems(self.TypeDict.keys())
        self.ui.inputAComboBox.addItems(self.TypeDict[self.ui.dataTypeComboBox.currentText()].keys())
        self.ui.inputBComboBox.addItems(self.TypeDict[self.ui.dataTypeComboBox.currentText()].keys())

        self.ui.dataTypeComboBox.currentTextChanged.connect(self.dataTypeChanged)

        self.ui.calcBtn.clicked.connect(self.calculate)
    
    def dataTypeChanged(self):
        self.ui.inputAComboBox.clear()
        self.ui.inputBComboBox.clear()
        self.ui.inputAComboBox.addItems(self.TypeDict[self.ui.dataTypeComboBox.currentText()].keys())
        self.ui.inputBComboBox.addItems(self.TypeDict[self.ui.dataTypeComboBox.currentText()].keys())

    def calculate(self):
        value = self.ui.inputAEditLine.text()
        if value == '':
            return
        
        currentType = self.ui.inputAComboBox.currentText()
        transType = self.ui.inputBComboBox.currentText()

        standardValue = float(value) * self.TypeDict[self.ui.dataTypeComboBox.currentText()][currentType]
        result = standardValue / self.TypeDict[self.ui.dataTypeComboBox.currentText()][transType]

        self.ui.orginDataLabel.setText(f'{value} {currentType} =')
        self.ui.transDataLabel.setText(f'{result} {transType}')
        self.ui.inputBEditLine.setText(str(result))



if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()