# Python Learning Project

このプロジェクトは、Python の基本的な学習を目的としたサンプルコードやスクリプトを含むリポジトリです。Docker を使用して環境を簡単にセットアップし、実行することができます。

## セットアップ手順

1. リポジトリをクローンします。
   ```bash
   git clone https://github.com/your-org/python-intro-series.git
   cd python-intro-series
   ```

2. Docker コンテナをビルドして起動します。
   ```bash
   docker-compose up -d --build
   ```

3. コンテナ内に入ります。
   ```bash
   docker-compose exec python bash
   ```

4. `src` ディレクトリに移動して、Python スクリプトを実行します。
   ```bash
   cd src
   python 2-1.basic_variables.py
   ```

## プロジェクト構成

```
python-learning/
├── docker-compose.yml   # Docker Compose 設定ファイル
├── Dockerfile           # Docker イメージの設定ファイル
├── requirements.txt     # Python パッケージの依存関係
├── src/                 # Python スクリプトが格納されるディレクトリ
│   ├── 2-1.basic_variables.py
│   ├── ...
│   └── output/          # 実行結果が保存されるディレクトリ (Git 管理外)
└── README.md            # このファイル
```

## 注意事項

- `src/output/` ディレクトリはプログラムの実行結果を保存する場所です。このディレクトリは `.gitignore` によって Git の管理対象外となっています。
- 必要に応じて `requirements.txt` に依存関係を追加してください。

## トラブルシューティング

- **Docker が正しく動作しない場合**  
  Docker がインストールされていることを確認し、以下のコマンドでサービスを再起動してください。
  ```bash
  docker-compose down
  docker-compose up -d --build
  ```

- **Python スクリプトのエラー**  
  必要な依存関係がインストールされているか確認してください。
  ```bash
  pip install -r requirements.txt
  ```

## ライセンス

このプロジェクトは [MIT ライセンス](LICENSE) のもとで公開されています。