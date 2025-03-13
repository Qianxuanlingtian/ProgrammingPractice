import markdown
from pathlib import Path

def convert_md_to_html(md_file_path, html_file_path):
    """
    将Markdown文件转换为HTML文件
    
    参数:
    md_file_path (str): 输入的Markdown文件路径
    html_file_path (str): 输出的HTML文件路径
    """
    # 读取Markdown文件内容
    with open(md_file_path, 'r', encoding='utf-8') as md_file:
        md_content = md_file.read()
    
    # 将Markdown转换为HTML，启用扩展
    html_content = markdown.markdown(md_content, extensions=[
        'fenced_code',  # 支持代码块
        'tables',       # 支持表格
        'toc',          # 支持目录
        'nl2br',        # 换行转换为<br>
        'sane_lists'    # 更智能的列表处理
    ])
    
    # 添加完整的HTML文档结构
    css_path = Path('resoucse/style.css').resolve().relative_to(Path.cwd())
    full_html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Markdown 预览</title>
    <link rel="stylesheet" href="{css_path}">
</head>
<body>
{html_content}
</body>
</html>"""
    
    # 将HTML内容写入文件
    with open(html_file_path, 'w', encoding='utf-8') as html_file:
        html_file.write(full_html)
