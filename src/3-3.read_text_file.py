# 3-3.read_text_file.py

file_path = "output/sample.txt"

try:
    with open(file_path, "r", encoding="utf-8") as f:
        contents = f.read()
        print("ファイルの中身:")
        print(contents)
except FileNotFoundError:
    print("ファイルが存在しません。")
