from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QApplication, QWidget

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('主窗口')
        self.resize(QSize(800, 600))

        # 窗体上下文菜单策略
        self.setContextMenuPolicy(Qt.ContextMenuPolicy.ActionsContextMenu)
        
        self.openFileAction = QAction('打开文件', self)
        self.closeFileAction = QAction('关闭文件', self)
        self.exitAction = QAction('退出', self)

        self.addActions([self.openFileAction, self.closeFileAction, self.exitAction])

        self.bind()

    def bind(self):
        self.openFileAction.triggered.connect(self.openFile)
        self.closeFileAction.triggered.connect(self.closeFile)
        self.exitAction.triggered.connect(self.close)

    def openFile(self):
        pass

    def closeFile(self):
        pass

if __name__ == "__main__":
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()