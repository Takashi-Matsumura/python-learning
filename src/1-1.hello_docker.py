# 1-1.hello_docker.py

import platform
import sys

print("🐍 Python 環境が正しく動作しています。")
print("- Pythonバージョン:", sys.version)
print("- 実行環境:", platform.system(), platform.machine())
print("- 実行モード: Dockerコンテナ内")
