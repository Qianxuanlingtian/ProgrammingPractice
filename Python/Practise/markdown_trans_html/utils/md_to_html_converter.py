import os
import shutil
from pathlib import Path
from markdown import markdown

# 将Markdown文件转换为html文件
def convert_md_to_html(md_folder, html_folder):
    """
    md_folder: Markdown文件路径;
    html_folder: html文件路径
    """
    # 指定样式文件
    css_path = Path('resoucse/style.css').resolve().relative_to(Path.cwd())
    print('css_path:', css_path)

    # 确保输出文件夹存在
    Path(html_folder).mkdir(parents=True, exist_ok=True)

    # 遍历所有文件夹及其子文件夹
    for dirpath, dirnames, filenames in os.walk(md_folder):
        # 计算相对路径
        relative_path = os.path.relpath(dirpath, md_folder)
        # 创建对应的输出文件夹
        output_dir = os.path.join(html_folder, relative_path)
        Path(output_dir).mkdir(parents=True, exist_ok=True)
        
        # 处理每个文件
        for file in filenames:
            file_path = os.path.join(dirpath, file)
            if file.endswith('.md'):
                # 读取md文件
                with open(file_path, 'r', encoding='utf-8') as f:
                    md_content = f.read()
                
                # 转换为html
                html_content = markdown(md_content, extensions=[
                    'fenced_code',  # 支持代码块
                    'tables',       # 支持表格
                    'toc',          # 支持目录
                    'nl2br',        # 换行转换为<br>
                    'mdx_truly_sane_lists',  # 更好的列表处理
                    'pymdownx.tasklist'  # 支持待办事项
                ])
                
                # 添加完整的HTML文档结构
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

                # 写入html文件
                html_file = os.path.splitext(file)[0]+'.html'
                html_path = os.path.join(output_dir, html_file)
                with open(html_path, 'w', encoding='utf-8') as f:
                    f.write(full_html)
            else:
                # 拷贝非md文件
                other_file_path = os.path.join(output_dir, file)
                shutil.copy2(file_path, other_file_path)


