from PySide6.QtWidgets import QApplication, QWidget, QComboBox, QVBoxLayout

class myWindow(QWidget):
    def __init__(self):
        super().__init__()
        mainLayout = QVBoxLayout()
        self.setLayout(mainLayout)
        cb = QComboBox()
        cb.addItems(['a', 'b', 'c', 'd'])
        cb.currentIndexChanged.connect(lambda: print(cb.currentText()))
        mainLayout.addWidget(cb)



if __name__ == '__main__':
    app = QApplication([])
    window = myWindow()
    window.show()
    app.exec()    