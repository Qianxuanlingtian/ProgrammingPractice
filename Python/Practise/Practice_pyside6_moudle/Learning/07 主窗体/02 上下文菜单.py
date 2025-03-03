from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QFileDialog, QLineEdit

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('主窗口')
        self.resize(QSize(800, 600))

        self.mainLayout = QVBoxLayout(self)
        self.setLayout(self.mainLayout)

        # 窗体上下文菜单策略
        self.setContextMenuPolicy(Qt.ContextMenuPolicy.ActionsContextMenu)
        
        self.openFileAction = QAction('打开文件', self)
        self.closeFileAction = QAction('关闭文件', self)
        self.exitAction = QAction('退出', self)

        self.addActions([self.openFileAction, self.closeFileAction, self.exitAction])

        self.ledtEdit = QLineEdit(self)
        self.ledtEdit.setPlaceholderText('请输入文本')
        # 控件上下文菜单策略
        self.ledtEdit.setContextMenuPolicy(Qt.ContextMenuPolicy.ActionsContextMenu)

        self.ledtEditTextCopy = QAction('复制', self)
        self.ledtEditTextCut = QAction('剪切', self)
        self.ledtEditTextAllDelete = QAction('全部删除', self)

        self.ledtEdit.addActions([self.ledtEditTextCopy, self.ledtEditTextCut, self.ledtEditTextAllDelete])

        self.bind()

    def bind(self):
        self.openFileAction.triggered.connect(self.openFile)
        self.closeFileAction.triggered.connect(self.closeFile)
        self.exitAction.triggered.connect(self.close)

        self.ledtEditTextCopy.triggered.connect(self.textCopy)
        self.ledtEditTextCut.triggered.connect(self.textCut)
        self.ledtEditTextAllDelete.triggered.connect(self.textAllDelete)

    def openFile(self):
        (self.selectedFiles, self.selectFileFilter) = QFileDialog.getOpenFileNames(self, '选择文件', './', '所有文件(*)')
        print('所选择的文件为：')
        for _ in self.selectedFiles:
            print(_)
        print(f'所属文件分类为：{self.selectFileFilter}')

    def closeFile(self):
        pass

    def textCopy(self):
        pass

    def textCut(self):
        pass

    def textAllDelete(self):
        pass

if __name__ == "__main__":
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()