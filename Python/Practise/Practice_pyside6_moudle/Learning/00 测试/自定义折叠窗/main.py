import sys
from PySide6.QtWidgets import (QApplication, QWidget, QVBoxLayout, 
                               QPushButton, QScrollArea, QFormLayout, QLabel, 
                               QLineEdit, QSpinBox, QCheckBox, QSlider)
from PySide6.QtCore import Qt, QSize

class ToolPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # 初始化状态变量
        self.is_expanded = True  # 当前是否展开
        
        # 创建界面元素
        self.setup_ui()
    
    def setup_ui(self):
        """初始化用户界面"""
        # 主垂直布局
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)  # 移除边距
        self.main_layout.setSpacing(0)
        
        # 创建折叠按钮
        self.btn_fold = QPushButton("V", self)  # 初始显示向下箭头
        self.btn_fold.setFixedSize(QSize(20, 20))  # 固定按钮大小
        self.btn_fold.clicked.connect(self.toggle_fold)  # 连接点击信号
        
        # 创建标题栏容器
        title_widget = QWidget()
        title_layout = QVBoxLayout(title_widget)
        title_layout.setContentsMargins(0, 0, 0, 0)
        title_layout.addWidget(self.btn_fold, 0, Qt.AlignmentFlag.AlignLeft)  # 按钮左对齐
        
        # 创建滚动区域（用于内容过多时滚动）
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)  # 自动调整内部widget大小
        
        # 创建内容容器（存放用户添加的控件）
        self.content_widget = QWidget()
        self.content_layout = QFormLayout(self.content_widget)
        self.content_layout.setContentsMargins(10, 5, 10, 10)  # 设置内容边距
        
        # 将内容容器放入滚动区域
        self.scroll_area.setWidget(self.content_widget)
        
        # 将标题栏和滚动区域添加到主布局
        self.main_layout.addWidget(title_widget)
        self.main_layout.addWidget(self.scroll_area)
        
        # 初始展开状态
        self.update_fold_state()

    def add_widget(self, title, widget):
        """
        添加带标题的控件
        参数:
            title (str): 左侧标题文本
            widget (QWidget): 要添加的右侧控件
        """
        self.content_layout.addRow(QLabel(title), widget)

    def toggle_fold(self):
        """切换折叠/展开状态"""
        self.is_expanded = not self.is_expanded
        self.update_fold_state()

    def update_fold_state(self):
        """根据当前状态更新界面显示"""
        # 控制内容区域的显示/隐藏
        self.scroll_area.setVisible(self.is_expanded)
        
        # 更新按钮文本（箭头方向）
        self.btn_fold.setText("V" if self.is_expanded else ">")

    def expand(self):
        """强制展开"""
        if not self.is_expanded:
            self.toggle_fold()

    def collapse(self):
        """强制折叠"""
        if self.is_expanded:
            self.toggle_fold()

class ToolBox(QWidget):
    def __init__(self):
        super().__init__()
        self.mainLayout = QVBoxLayout(self)

        # 创建滚动区域（用于内容过多时滚动）
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)  # 自动调整内部widget大小

        # 创建滚动区域内容widget
        self.content_Widget = QWidget(self)
        self.content_Layout = QVBoxLayout(self)
        self.content_Widget.setLayout(self.content_Layout)

        self.scroll_area.setWidget(self.content_Widget)

        self.mainLayout.addWidget(self.scroll_area)

        self.setLayout(self.mainLayout)

    def add_Widget(self, wg:ToolPage):
        self.content_Layout.addWidget(wg)

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.mainLayout = QVBoxLayout(self)
        self.tool_Box = ToolBox()
        
        self.tool_Page1 = ToolPage()
        self.tool_Page1.add_widget('姓名', QLineEdit())
        self.tool_Page1.add_widget('年龄', QSpinBox())

        self.tool_Page2 = ToolPage()
        self.tool_Page2.add_widget('启用', QCheckBox('启用功能'))
        self.tool_Page2.add_widget('透明度', QSlider(Qt.Orientation.Horizontal))

        self.tool_Page3 = ToolPage()
        self.tool_Page3.add_widget('启用', QCheckBox('启用功能'))
        self.tool_Page3.add_widget('透明度', QSlider(Qt.Orientation.Horizontal))

        self.tool_Page4 = ToolPage()
        self.tool_Page4.add_widget('启用', QCheckBox('启用功能'))
        self.tool_Page4.add_widget('透明度', QSlider(Qt.Orientation.Horizontal))

        self.tool_Box.add_Widget(self.tool_Page1)
        self.tool_Box.add_Widget(self.tool_Page2)
        self.tool_Box.add_Widget(self.tool_Page3)
        self.tool_Box.add_Widget(self.tool_Page4)

        self.mainLayout.addWidget(self.tool_Box)
        self.setLayout(self.mainLayout)
        

if __name__ == "__main__":
    # # 测试代码
    # app = QApplication(sys.argv)
    
    # # 创建示例窗口
    # window = QWidget()
    # layout = QVBoxLayout(window)
    
    

    # # 创建两个可折叠面板
    # panel1 = ToolPage()
    # panel1.add_widget("姓名", QLineEdit())
    # panel1.add_widget("年龄", QSpinBox())
    
    # panel2 = ToolPage()
    # panel2.add_widget("启用", QCheckBox("启用功能"))
    # panel2.add_widget("透明度", QSlider(Qt.Orientation.Horizontal))

    # panel3 = ToolPage()
    # panel3.add_widget("启用", QCheckBox("启用功能"))
    # panel3.add_widget("透明度", QSlider(Qt.Orientation.Horizontal))

    # panel4 = ToolPage()
    # panel4.add_widget("启用", QCheckBox("启用功能"))
    # panel4.add_widget("透明度", QSlider(Qt.Orientation.Horizontal))

    # panel5 = ToolPage()
    # panel5.add_widget("启用", QCheckBox("启用功能"))
    # panel5.add_widget("透明度", QSlider(Qt.Orientation.Horizontal))
    
    # # 添加到主布局
    # layout.addWidget(panel1)
    # layout.addWidget(panel2)
    # layout.addWidget(panel3)
    # layout.addWidget(panel4)
    # layout.addWidget(panel5)
    # layout.addStretch()
    
    # window.resize(300, 400)
    # window.show()
    # sys.exit(app.exec())
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()