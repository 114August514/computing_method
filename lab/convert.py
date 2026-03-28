from nbconvert import MarkdownExporter

# 配置
from_path = "lab/lab2/lab2.ipynb"
to_path = "lab/lab2/lab2.md"

def convert_notebook_to_markdown(notebook_path, output_path):
    exporter = MarkdownExporter()
    body, resources = exporter.from_filename(notebook_path)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(body)
    print(f"Converted: {notebook_path} → {output_path}")

if __name__ == "__main__":
    convert_notebook_to_markdown(from_path, to_path)
