from PySide6.QtWidgets import QApplication, QMainWindow
from Ui_file_read_write import Ui_MainWindow

class myWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication([])
    window = myWindow()
    window.show()
    app.exec()