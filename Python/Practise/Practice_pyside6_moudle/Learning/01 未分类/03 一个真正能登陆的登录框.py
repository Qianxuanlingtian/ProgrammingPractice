from PySide6.QtWidgets import QApplication, QWidget, QPushButton
from Ui_login import Ui_Form

class MyWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.loginFunc)

    def loginFunc(self):
        # 拿到账号
        account = self.lineEdit.text()
        # 拿到密码
        password = self.lineEdit_2.text()

        if account == '123' and password == '123':
            print('登录成功')
        else:
            print('登录失败')


if __name__ == "__main__":
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()