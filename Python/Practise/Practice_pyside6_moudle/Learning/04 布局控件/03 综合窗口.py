from PySide6.QtCore import Qt, QSize
from PySide6.QtWidgets import (QApplication, QWidget, 
                               QVBoxLayout, QGridLayout,
                               QButtonGroup,
                               QPushButton, QLabel, QComboBox, QSlider, QLineEdit, 
                               QCheckBox, QRadioButton, QTextEdit, QPlainTextEdit)

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        self.mainLayout = QVBoxLayout(self)

        self.lb1 = QLabel(u'标签1', self)
        self.lb1.setText('标签1被修改了')
        self.lb1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.btn1 = QPushButton(u'按钮1', self)

        self.lineEdit1 = QLineEdit('', self)
        self.lineEdit1.setPlaceholderText('请输入内容')
        self.lineEdit1.setEchoMode(QLineEdit.EchoMode.Password)

        self.checkBox1 = QCheckBox('复选框1', self)
        self.checkBox1.setCheckable(False)
        self.checkBox2 = QCheckBox('复选框2', self)
        self.checkBox2.setChecked(True)

        self.genderNan = QRadioButton('男', self)
        self.genderNv = QRadioButton('女', self)

        self.favoriteGroup = QButtonGroup(self)
        self.radiobtnMath = QRadioButton('数学', self)
        self.radiobtnChinese = QRadioButton('语文', self)
        self.radiobtnEnglish = QRadioButton('英语', self)
        self.favoriteGroup.addButton(self.radiobtnMath)
        self.favoriteGroup.addButton(self.radiobtnChinese)
        self.favoriteGroup.addButton(self.radiobtnEnglish)

        self.cb1 = QComboBox(self)
        self.cb1.setPlaceholderText('请选择')
        self.cb1.addItems(['选项1', '选项2', '选项3'])
        self.cb1.removeItem(0)

        markdownStr = """
# 标题1
## 标题2
```python
def hello():
    return 'hello'
```
- 1
- 2
- 3
---
这是一段正常文字
"""
        htmlStr = """
<h1>标题1</h1><p1>这是一段正常文字</p1>
"""

        self.richText = QTextEdit(self)
        self.richText.setPlaceholderText('请输入内容')
        # self.richText.setMarkdown(markdownStr)
        # self.richText.setHtml(htmlStr)
        self.richText.setPlainText('这是一段普通文字')

        self.plainText = QPlainTextEdit(self)
        self.plainText.setPlainText('这是一段普通文字')

        self.slider = QSlider(Qt.Orientation.Horizontal, self)
        self.slider.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.slider.setTickInterval(10)
        self.slider.setRange(0, 200)

        self.mainLayout.addWidget(self.lb1)
        self.mainLayout.addWidget(self.lineEdit1)
        self.mainLayout.addWidget(self.btn1)
        self.mainLayout.addWidget(self.cb1)
        self.mainLayout.addWidget(self.checkBox1)
        self.mainLayout.addWidget(self.checkBox2)
        self.mainLayout.addWidget(self.genderNan)
        self.mainLayout.addWidget(self.genderNv)
        self.mainLayout.addWidget(self.radiobtnMath)
        self.mainLayout.addWidget(self.radiobtnChinese)
        self.mainLayout.addWidget(self.radiobtnEnglish)
        self.mainLayout.addWidget(self.richText)
        self.mainLayout.addWidget(self.plainText)
        self.mainLayout.addWidget(self.slider)

        self.setLayout(self.mainLayout)

        self.bind()

    def bind(self):
        self.btn1.clicked.connect(lambda: print('按钮1被点击了'))
        self.lineEdit1.textChanged.connect(self.text_Changed)
        self.lineEdit1.returnPressed.connect(self.return_Pressed)
        self.checkBox2.stateChanged.connect(lambda: print(f'复选框2的状态是：{self.checkBox2.isChecked()}'))
        self.checkBox2.stateChanged.connect(self.checkBox2_StateChanged)
        self.cb1.currentIndexChanged.connect(lambda: print(f'当前选中的是：{self.cb1.currentText()}'))

        # 单选按钮的信号与槽的绑定
        self.genderNan.clicked.connect(lambda: print(f'性别是{self.genderNan.text()}'))
        self.genderNv.clicked.connect(lambda: print(f'性别是{self.genderNv.text()}'))

        self.favoriteGroup.buttonClicked.connect(self.which_btn_clicked)
        
        self.richText.textChanged.connect(lambda: print(f'文本框的内容是：{self.richText.toPlainText()}'))

        self.slider.valueChanged.connect(lambda value: print(f'滑块的值是：{value}'))

    def text_Changed(self, text):
        print(f'文本框发生了改变：{text}')
    
    def return_Pressed(self):
        print('文本框按回车了')
        print(f'文本框的内容是：{self.lineEdit1.text()}')

    def checkBox2_StateChanged(self, state):
        print(f'复选框2的状态是：{state}')

    def which_btn_clicked(self):
        print('按钮被选中了')
        print(f'选中的按钮是：{self.favoriteGroup.checkedButton().text()}')

if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()