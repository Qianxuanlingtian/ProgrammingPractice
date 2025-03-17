import os
from pathlib import Path
from utils.md_to_html_converter import convert_md_to_html

if __name__ == "__main__":
    in_path = os.path.join(Path.cwd(), 'mark')
    out_path = os.path.join(Path.cwd(), 'html')
    convert_md_to_html(in_path, out_path)