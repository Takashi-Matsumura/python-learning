FROM python:3.12-slim

WORKDIR /app

# requirements.txt を先にコピーすることでキャッシュを活用
COPY requirements.txt /app/

# ライブラリをインストール
RUN pip install --upgrade pip && pip install -r requirements.txt

# アプリケーションのコードをコピー
COPY . /app

CMD ["bash"]
