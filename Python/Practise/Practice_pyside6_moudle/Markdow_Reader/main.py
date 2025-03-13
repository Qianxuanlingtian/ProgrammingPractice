import os
from pathlib import Path
from PySide6.QtCore import Qt, QUrl, QSize
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog, QMessageBox
from PySide6.QtGui import QTextDocument
from ui.Ui_main_window import Ui_MainWindow
from markdown import markdown
from utils.markdown_parser import convert_md_to_html

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.bind()
    
    def bind(self):
        self.actionOpen.triggered.connect(self.fileOpen)
        self.actionAbout.triggered.connect(self.helpAbout)

    def fileOpen(self):
        (file_Path, type) = QFileDialog.getOpenFileName(self, '请选择文件', './','MarkDown文件(*.md);;文本文件(*.txt);;所有文件(*)', 
                                           selectedFilter= 'MarkDown文件(*.md)', options=QFileDialog.Options())
        self.readFile(file_Path, type)

    def readFile(self, file_path, file_type):
        # self.read_direct(file_path, file_type)
        self.read_markdown(file_path, file_type)

    def read_direct(self, file_path, file_type):
        if file_type == 'MarkDown文件(*.md)':
            self.textBrowser.setSource(QUrl.fromLocalFile(file_path), QTextDocument.ResourceType.MarkdownResource)
        elif file_type == '文本文件(*.txt)':
            with open(file_path, 'r', encoding='utf-8') as f:
                self.textBrowser.setText(f.read())
        else:
            self.textBrowser.setSource(QUrl.fromLocalFile(file_path), QTextDocument.ResourceType.UnknownResource)

    def read_markdown(self, file_path, file_type):
        if file_type == 'MarkDown文件(*.md)':
            with open(file_path, 'r', encoding='utf-8') as f:
                markdown_content = f.read()
                html_content = markdown(markdown_content, extensions=[
                    'fenced_code',  # 支持代码块
                    'tables',       # 支持表格
                    'toc',          # 支持目录
                    'nl2br',        # 换行转换为<br>
                    'sane_lists'    # 更智能的列表处理
                ])
                
                # 添加基本样式
                styled_html = f"""
                <html>
                    <head>
                        <link rel="stylesheet" href="resoucse/style.css">
                    </head>
                    <body>
                        {html_content}
                    </body>
                </html>
                """
                self.textBrowser.setHtml(styled_html)
            convert_md_to_html(file_path, Path('outhtml.html'))

    def helpAbout(self):
        self.helpAboutMessage = QMessageBox()
        self.helpAboutMessage.setWindowTitle(u'关于')
        self.helpAboutMessage.show()


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
