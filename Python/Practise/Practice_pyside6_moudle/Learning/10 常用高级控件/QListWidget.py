from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QFont, QAction
from PySide6.QtWidgets import QApplication, QWidget, QStyle, QVBoxLayout, QHBoxLayout, QListWidget, QListWidgetItem, QPushButton
from faker import Faker
import random

class Window1(QWidget):
    """QListWidget的增删插改查"""
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QListWidget的增删插改查')
        self.move(400, 300)
        self.mainLayout = QVBoxLayout(self)
        self.setLayout(self.mainLayout)

        self.listWidget = QListWidget(self)
        # 增
        self.listWidget.addItem(QListWidgetItem(u'测试'))
        self.listWidget.addItems([str(i) for i in range(20)])
        # 插
        self.listWidget.insertItem(2, '你好')
        # 改
        self.listWidget.item(4).setText('更改')
        # 删
        self.listWidget.takeItem(5)
        # 找
        # 标签主要使用的包含：
        # - MatchContains 搜索词中包含在项目中
        # - MatchStartsWith 以XX开头
        # - MatchCaseSensitive 搜索英文的时候是否区分大小写
        # - MatchRegularExpression 以正则搜索
        result = self.listWidget.findItems('17', Qt.MatchFlag.MatchContains)
        for i in result:
            print(i.text())

        # self.listWidget.clear()

        self.btn = QPushButton('全部删除')
        self.btn.clicked.connect(lambda: self.listWidget.clear())

        self.mainLayout.addWidget(self.listWidget)
        self.mainLayout.addWidget(self.btn)

class Window2(QWidget):
    """QListWidget的排序"""
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QListWidget的排序')
        self.move(700, 300)
        self.mainLayout = QVBoxLayout(self)
        self.setLayout(self.mainLayout)

        self.listWidget = QListWidget(self)
        self.listWidget.addItems([str(random.randint(0, 100)) for _ in range(20)])

        self.btn = QPushButton('升序排列')
        # 对列表进行排序
        self.btn.clicked.connect(lambda: self.listWidget.sortItems(Qt.SortOrder.AscendingOrder))
        self.btn1 = QPushButton('降序排列')
        self.btn1.clicked.connect(lambda: self.listWidget.sortItems(Qt.SortOrder.DescendingOrder))

        self.btnLayout = QHBoxLayout()
        self.btnLayout.addWidget(self.btn)
        self.btnLayout.addWidget(self.btn1)

        self.mainLayout.addWidget(self.listWidget)
        self.mainLayout.addLayout(self.btnLayout)

class Window3(QWidget):
    """QListWidget的上下文菜单"""
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QListWidget的上下文菜单')
        self.move(1000, 300)

        self.fake = Faker(locale = 'zh_CN')

        self.mainLayout = QVBoxLayout(self)
        self.setLayout(self.mainLayout)

        self.listWidget = QListWidget(self)
        self.listWidget.addItems([self.fake.name() for _ in range(20)])

        # 给窗体添加上下文菜单
        self.sayHello = QAction('你好')
        self.setContextMenuPolicy(Qt.ContextMenuPolicy.ActionsContextMenu)
        self.addAction(self.sayHello)

        # 给控件添加上下文菜单
        self.outputSelectedItem = QAction("输出当前选中的值")
        self.listWidget.setContextMenuPolicy(Qt.ContextMenuPolicy.ActionsContextMenu)
        self.listWidget.addAction(self.outputSelectedItem)
        self.deleteCurrentItem = QAction("删除当前值")
        self.listWidget.addAction(self.deleteCurrentItem)

        # 将第一个元素设置为能够选中给元素
        self.listWidget.item(0).setCheckState(Qt.CheckState.Unchecked)

        self.mainLayout.addWidget(self.listWidget)

        self.bind()
    
    def bind(self):
        self.listWidget.currentItemChanged.connect(self.currItemChange)
        self.listWidget.itemChanged.connect(self.itemChange)
        self.sayHello.triggered.connect(lambda: print("你好"))
        self.outputSelectedItem.triggered.connect(self.outputSeclectedItemText)
        self.deleteCurrentItem.triggered.connect(lambda: self.listWidget.takeItem(self.listWidget.currentRow()))

    def currItemChange(self, item):
        print(f'当前选择的值是：{item.text()}')
    
    def itemChange(self):
        print(f'{self.listWidget.currentItem().text()}被选中了！')
        print(self.listWidget.currentItem().checkState())


    def outputSeclectedItemText(self):
        print(self.listWidget.currentItem().text())

if __name__ == '__main__':
    app = QApplication([])
    window1 = Window1()
    window1.show()
    window2 = Window2()
    window2.show()
    window3 = Window3()
    window3.show()
    app.exec()