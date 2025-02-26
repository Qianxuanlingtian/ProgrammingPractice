from PySide6.QtCore import Qt, QSize
from PySide6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QGridLayout,
                               QPushButton, QLabel, QComboBox, QSlider, QLineEdit, 
                               QCheckBox, QRadioButton)

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        self.mainLayout = QVBoxLayout(self)

        self.lb1 = QLabel(u'标签1', self)
        self.lb1.setText('标签1被修改了')
        self.lb1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.btn1 = QPushButton(u'按钮1', self)
        self.btn1.clicked.connect(lambda: print('按钮1被点击了'))

        self.lineEdit1 = QLineEdit('', self)
        self.lineEdit1.setPlaceholderText('请输入内容')
        self.lineEdit1.setEchoMode(QLineEdit.EchoMode.Password)
        self.lineEdit1.textChanged.connect(self.text_Changed)
        self.lineEdit1.returnPressed.connect(self.return_Pressed)

        self.checkBox1 = QCheckBox('复选框1', self)
        self.checkBox1.setCheckable(False)
        self.checkBox2 = QCheckBox('复选框2', self)
        self.checkBox2.setChecked(True)
        self.checkBox2.stateChanged.connect(lambda: print(f'复选框2的状态是：{self.checkBox2.isChecked()}'))
        self.checkBox2.stateChanged.connect(self.checkBox2_StateChanged)


        self.cb1 = QComboBox(self)
        self.cb1.setPlaceholderText('请选择')
        self.cb1.addItems(['选项1', '选项2', '选项3'])
        self.cb1.removeItem(0)
        self.cb1.currentIndexChanged.connect(lambda: print(f'当前选中的是：{self.cb1.currentText()}'))

        self.mainLayout.addWidget(self.lb1)
        self.mainLayout.addWidget(self.lineEdit1)
        self.mainLayout.addWidget(self.btn1)
        self.mainLayout.addWidget(self.cb1)
        self.mainLayout.addWidget(self.checkBox1)
        self.mainLayout.addWidget(self.checkBox2)

        self.setLayout(self.mainLayout)

    def text_Changed(self, text):
        print(f'文本框发生了改变：{text}')
    
    def return_Pressed(self):
        print('文本框按回车了')
        print(f'文本框的内容是：{self.lineEdit1.text()}')

    def checkBox2_StateChanged(self, state):
        print(f'复选框2的状态是：{state}')

if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()