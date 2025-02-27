from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QMessageBox, QPushButton
from PySide6.QtCore import Qt

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QMessageTest')
        self.resize(400, 300)

        self.mainLayout = QVBoxLayout(self)
        self.setLayout(self.mainLayout)

        self.btn = QPushButton('按钮', self)

        self.mainLayout.addWidget(self.btn)

        self.bind()

    def bind(self):
        self.btn.clicked.connect(self.showDialog)

    def showDialog(self):
        # 按使用频率排序
        # QMessageBox.information(self, '信息', '这是一个信息对话框')
        # QMessageBox.question(self, '问题', '这是一个问题对话框')
        # QMessageBox.warning(self, '警告', '这是一个警告对话框')
        # QMessageBox.critical(self, '错误', '这是一个错误对话框')
        # QMessageBox.about(self, '关于', '这是一个关于对话框')
        # QMessageBox.aboutQt(self, '关于Qt')
        
        messageBox = QMessageBox(self)
        
        # 设置按钮文本
        okButton = messageBox.addButton("确定", QMessageBox.ButtonRole.AcceptRole)
        cancelButton = messageBox.addButton("取消", QMessageBox.ButtonRole.RejectRole)
        yesButton = messageBox.addButton("是", QMessageBox.ButtonRole.YesRole)
        noButton = messageBox.addButton("否", QMessageBox.ButtonRole.NoRole)
        closeButton = messageBox.addButton("关闭", QMessageBox.ButtonRole.DestructiveRole)
        abortButton = messageBox.addButton("中止", QMessageBox.ButtonRole.ActionRole)

        messageBox.setWindowTitle('标题')
        messageBox.setText('内容')

        messageBox.exec()

        reply = messageBox.clickedButton()

        if reply == okButton:
            print('你点击了：确定')
        elif reply == cancelButton:
            print('你点击了：取消')
        elif reply == yesButton:
            print('你点击了：是')
        elif reply == noButton:
            print('你点击了：否')
        elif reply == closeButton:
            print('你点击了：关闭')
        elif reply == abortButton:
            print('你点击了：中止')

if __name__ == "__main__":
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()