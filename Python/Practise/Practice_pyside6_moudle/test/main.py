import sys
from PySide6.QtWidgets import QApplication, QMainWindow
# Pyside6-uic main_window.ui -o ui_main_window.py
from ui_main_window import Ui_MainWindow

import time
from threading import Thread
from task import add
from user_signal import my_signal


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow() # UI类的实例化（）
        self.ui.setupUi(self)
    
        # 连接信号与槽
        self.bind()

    def bind(self):
        # self.ui.___ACTION___.triggered.connect(___FUNCTION___)
        # self.ui.___BUTTON___.clicked.connect(___FUNCTION___)
        # self.ui.___COMBO_BOX___.currentIndexChanged.connect(___FUNCTION___)
        # self.ui.___SPIN_BOX__.valueChanged.connect(___FUNCTION___)
        # 自定义信号.属性名.connect(___FUNCTION___)
        self.ui.pushButton.clicked.connect(self.handle_click)
        
        # 引入自定义信号
        my_signal.setProgressBar.connect(self.set_progress_bar)
        my_signal.setResult.connect(self.set_result)

    def set_progress_bar(self, progress: int):
        self.ui.progressBar.setValue(progress)

    def set_result(self, result: str):
        self.ui.result.setText(result)

    def handle_click(self):
        def innerFunction():
            # 获取加数和被加数的值
            a = self.ui.inputA.value()
            b = self.ui.inputB.value()

            # 获取延时
            time_cost = self.ui.timeCost.value()

            for index in range(time_cost):
                process = index * 100 // time_cost
                my_signal.setProgressBar.emit(process)
                time.sleep(1)
            my_signal.setProgressBar.emit(100)

            # 计算两数相加
            result = str(add(a, b))
            my_signal.setResult.emit(result)

        task = Thread(target=innerFunction)
        task.start()

    

if __name__ == "__main__":
    app = QApplication(sys.argv)  # 启动一个应用
    window = MainWindow()   # 实例化一个窗口
    window.show()   # 显示主窗口
    sys.exit(app.exec())  # 避免程序执行到这一步后直接退出