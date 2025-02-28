from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QMenuBar, QMenu,  
                               QVBoxLayout, QGridLayout, QHBoxLayout,
                               QPushButton, QLabel, QLineEdit, QComboBox, QTextEdit,
                               QPlainTextEdit, QMessageBox, QFileDialog)


class myWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 设置主窗体
        self.setObjectName('mainWindow')
        self.setWindowTitle('这是一个测试窗口')
        self.resize(QSize(800, 600))

        # 设置菜单栏        
        self.mmenuBar = QMenuBar(self)
        self.setMenuBar(self.mmenuBar)
        self.menuFile = QMenu('文件', self)
        self.mmenuBar.addMenu(self.menuFile)
        self.menuEdit = QMenu('编辑', self)
        self.mmenuBar.addMenu(self.menuEdit)
        self.menuHelp = QMenu('帮助', self)
        self.mmenuBar.addMenu(self.menuHelp)

        # 创建各菜单动作
        # 帮助菜单“关于”关于动作
        self.actionHelpAbout = QAction(self)
        self.actionHelpAbout.setText('关于')
        helpAboutIcon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.HelpAbout))
        self.actionHelpAbout.setIcon(helpAboutIcon)
        
        if self.actionHelpAbout.toggled:
            QMessageBox.information(self, '关于', '这是一个示例信息')

        # 为各菜单添加动作
        self.menuHelp.addAction(self.actionHelpAbout)
        
        # 设置窗体中心控件centerWG
        self.centerWG = QWidget(self)
        self.setCentralWidget(self.centerWG)
        
        # 创建布局
        self.centerMainLayout = QGridLayout(self.centerWG)  # 创建中心控件主布局
        self.testVBoxLayout = QVBoxLayout()
        self.testGridLayout = QGridLayout()

        # 向各个布局添加控件
        self.centerMainLayout.addWidget(QPushButton('确定'), 0, 0, 1, 1)
        self.testVBoxLayout.addWidget(QPushButton('测试'))
        self.testGridLayout.addWidget(QPushButton('1'), 0, 0, 1, 1)
        self.testGridLayout.addWidget(QPushButton('2'), 0, 1, 1, 1)
        self.testGridLayout.addWidget(QPushButton('3'), 0, 2, 1, 1)
        self.testGridLayout.addWidget(QPushButton('4'), 1, 0, 1, 1)
        self.testGridLayout.addWidget(QPushButton('5'), 1, 1, 1, 1)
        self.testGridLayout.addWidget(QPushButton('6'), 1, 2, 1, 1)
        self.testGridLayout.addWidget(QPushButton('7'), 2, 0, 1, 1)
        self.testGridLayout.addWidget(QPushButton('8'), 2, 1, 1, 1)
        self.testGridLayout.addWidget(QPushButton('9'), 2, 2, 1, 1)
        
        # 向窗体中心部件主布局添加其他布局
        self.centerMainLayout.addLayout(self.testVBoxLayout, 1, 0, 1, 2)
        self.centerMainLayout.addLayout(self.testGridLayout, 0, 1, 1, 1)

        # 设置中心控件主布局
        self.centerWG.setLayout(self.centerMainLayout)

if __name__ == "__main__":
    app = QApplication([])
    window = myWindow()
    window.show()
    app.exec()