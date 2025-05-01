# 3-1.create_folder_and_file.py

from pathlib import Path

output_dir = Path("output")
output_dir.mkdir(exist_ok=True)

file_path = output_dir / "sample.txt"
file_path.write_text("Pythonでファイルを作成しました。")

print(f"{file_path} を作成しました。")
