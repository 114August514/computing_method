from nbconvert import MarkdownExporter
import os

# 配置
from_path = "lab/lab4/lab4.ipynb"
to_path = "lab/lab4/lab4.md"

def convert_notebook_to_markdown(notebook_path, output_path):
    # 配置资源输出路径前缀
    assets_rel_path = "assets"
    exporter = MarkdownExporter()
    
    # 获取资源并进行转换
    body, resources = exporter.from_filename(
        notebook_path, resources={'output_files_dir': assets_rel_path}
    )
    
    # 写入 Markdown 文件
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(body)
    
    # 处理图片等资源
    if 'outputs' in resources:
        output_dir = os.path.dirname(output_path)
        for filename, data in resources['outputs'].items():
            resource_path = os.path.join(output_dir, filename)
            os.makedirs(os.path.dirname(resource_path), exist_ok=True)
            with open(resource_path, 'wb') as f:
                f.write(data)
            print(f"Saved resource: {resource_path}")

    print(f"Converted: {notebook_path} → {output_path}")

if __name__ == "__main__":
    convert_notebook_to_markdown(from_path, to_path)
