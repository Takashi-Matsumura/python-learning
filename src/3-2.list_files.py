# 3-2.list_files.py

from pathlib import Path

folder = Path("output")

if folder.exists():
    for file in folder.iterdir():
        print(file.name)
else:
    print("フォルダが存在しません。")
