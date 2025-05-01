# 5-1.download_image.py

import urllib.request

url = "https://upload.wikimedia.org/wikipedia/commons/9/9a/Pug_600.jpg"  # 犬の画像
output_path = "data/dog.jpg"
urllib.request.urlretrieve(url, output_path)

print(f"画像を {output_path} に保存しました。")
