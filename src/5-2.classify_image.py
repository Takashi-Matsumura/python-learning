# 5-2.classify_image.py

import torch
from torchvision import models, transforms
from PIL import Image

# 画像読み込み
img = Image.open("data/dog.jpg")

# 前処理（サイズ調整・正規化など）
preprocess = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),  # PIL → Tensor
    transforms.Normalize(mean=[0.485, 0.456, 0.406],
                         std=[0.229, 0.224, 0.225]),
])

input_tensor = preprocess(img).unsqueeze(0)  # バッチ次元を追加

# モデル準備
model = models.resnet18(pretrained=True)
model.eval()

# 推論
with torch.no_grad():
    output = model(input_tensor)
    predicted_idx = output.argmax().item()

# ラベルの読み込み
import json
from urllib.request import urlopen

LABELS_URL = "https://s3.amazonaws.com/deep-learning-models/image-models/imagenet_class_index.json"
class_idx = json.load(urlopen(LABELS_URL))
label = class_idx[str(predicted_idx)][1]

print(f"この画像は「{label}」と判定されました。")
