import json

# 读取 Jupyter Notebook 文件
notebook_path = "/mnt/data/Baseline.ipynb"#这里修改你的地址
with open(notebook_path, "r", encoding="utf-8") as file:
    notebook_content = json.load(file)

# 提取所有代码单元
code_cells = [cell["source"] for cell in notebook_content["cells"] if cell["cell_type"] == "code"]

# 合并代码并转换为字符串
python_code = "\n\n".join("".join(cell) for cell in code_cells)
python_code
