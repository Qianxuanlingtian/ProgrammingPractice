from PySide6.QtWidgets import QApplication, QWidget, QStyle, QVBoxLayout, QPushButton, QGridLayout
from PySide6.QtCore import QSize

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        # self.style().standardIcon(QStyle.StandardPixmap.SP_ArrowRight)
        self.setWindowTitle('显示所有的内置图标')
        self.resize(800, 600)
        self.mainLayout = QVBoxLayout()
        self.btnLayout = QGridLayout()

        currentRow = 0
        rowCount = 4
        for index, each in enumerate(QStyle.StandardPixmap):
            currentCol = index % rowCount

            # 用来显示的按钮
            btn = QPushButton()
            btn.setText(f'{str(index)}-{str(list(each))}')
            btn.setIcon(self.style().standardPixmap(each))
            btn.setIconSize(QSize(24, 24))

            # 每四行换一次行
            if currentCol == 0:
                currentRow += 1
            self.btnLayout.addWidget(btn, currentRow, currentCol)
        
        self.mainLayout.addLayout(self.btnLayout)
        self.setLayout(self.mainLayout)

if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()