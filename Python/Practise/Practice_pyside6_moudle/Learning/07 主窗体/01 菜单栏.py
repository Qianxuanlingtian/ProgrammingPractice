from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QMenu, QMessageBox, QFileDialog

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('主窗口')
        self.resize(QSize(800, 600))

        self.menu = self.menuBar()
        
        self.fileMenu = QMenu('文件', self)
        self.openFileAction = QAction('打开文件', self)
        self.closeFileAction = QAction('关闭文件', self)
        self.exitAction = QAction('退出', self)

        self.moreMenu = QMenu('更多', self)
        self.moreMenuAction1 = QAction('更多1', self)
        self.moreMenuAction2 = QAction('更多2', self)
        self.moreMenuAction3 = QAction('更多3', self)
        
        self.fileMenu.addActions([self.openFileAction, self.closeFileAction, self.exitAction])
        self.fileMenu.addMenu(self.moreMenu)
        self.moreMenu.addActions([self.moreMenuAction1, self.moreMenuAction2, self.moreMenuAction3])

        self.menu.addMenu(self.fileMenu)

        self.bind()
    
    def bind(self):
        # 文件菜单部分
        self.openFileAction.triggered.connect(self.openFile)
        self.closeFileAction.triggered.connect(self.closeFile)
        self.exitAction.triggered.connect(self.close)

    # 文件菜单部分
    # 打开文件
    def openFile(self):
        print(QFileDialog.getOpenFileNames(self, '打开文件', './', 'All Files (*)')[0][0])
        pass
    
    # 关闭文件
    def closeFile(self):
        pass

if __name__ == "__main__":
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()