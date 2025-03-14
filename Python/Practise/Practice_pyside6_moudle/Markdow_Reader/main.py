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
        self.read_markdown(file_path, file_type)

    def read_markdown(self, file_path, file_type):
        if file_type == 'MarkDown文件(*.md)':
            with open(file_path, 'r', encoding='utf-8') as f:
                markdown_content = f.read()
                # self.textEdit.setMarkdown(markdown_content)
                
                html_content = markdown(markdown_content, extensions=[
                    'fenced_code',  # 支持代码块
                    'tables',       # 支持表格
                    'toc',          # 支持目录
                    'nl2br',        # 换行转换为<br>
                    'pymdownx.tasklist',  # 支持待办事项
                    'mdx_truly_sane_lists'  # 更好的列表处理
                ])
                
                # 添加完整HTML结构和样式
                css_path = Path('resoucse/style.css').resolve().relative_to(Path.cwd())
                styled_html = f"""<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="{css_path}">
    </head>
    <body style="margin: 0; padding: 20px;">
        {html_content}
    </body>
</html>
                """
                self.textEdit.setHtml(styled_html)
                # textEdit
                self.textEdit.document().setDefaultStyleSheet(open(css_path, encoding='utf-8').read())
                self.textEdit.setStyleSheet("""
                    QTextEdit {
                        background-color: white;
                        color: #24292e;
                        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
                        font-size: 16px;
                        padding: 20px;
                    }
                """)
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
