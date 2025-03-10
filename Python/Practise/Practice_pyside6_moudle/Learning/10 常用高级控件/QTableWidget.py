from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QFont, QAction
from PySide6.QtWidgets import (QApplication, QWidget, QStyle, QVBoxLayout, 
                               QHBoxLayout, QTableWidget, QTableWidgetItem,
                               QHeaderView, QPushButton)
from faker import Faker
import random

class Window1(QWidget):
    """QTableWidget的增删插改查"""
    def __init__(self):
        super().__init__()
        self.move(100, 100)
        self.resize(800, 600)
        self.setWindowTitle('QListWidget的增删插改查')
        self.main_layout = QVBoxLayout(self)

        self.fake = Faker(locale='zh_CN')
        self.fake_data = [[self.fake.name(), self.fake.address(), self.fake.ascii_free_email()] for _ in range(80)]

        self.table_widget = QTableWidget(self)
        self.table_widget.setRowCount(80)
        self.table_widget.setColumnCount(3)
        self.table_widget.setHorizontalHeaderLabels(['姓名', '地址', '邮箱'])
        self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        for rowIndex, row in enumerate(self.fake_data):
            for colunmIndex, item in enumerate(row):
                self.table_widget.setItem(rowIndex, colunmIndex, QTableWidgetItem(item))

        self.main_layout.addWidget(self.table_widget)

if __name__ == '__main__':
    app = QApplication([])
    window1 = Window1()
    window1.show()  

    app.exec()