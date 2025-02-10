# BABELデータセットの可視化
BABELデータセットをLLMを用いて構築し、可視化を行うためのリポジトリ

## 環境構築
- ライブラリのインストール
```
poetry install
```
```
poetry shell
```
- 環境変数の設定
dotenvを使っているので
```
cp ./.env.example ./.env
```
してからOPENAI_API_KEYにAPI_KEYを置いておいてください
- promptの設定
./data/prompt/babel.txtにpromptを設定して書き込んでおいてください


## データの生成
```
python3 src/main.py
```

## ディレクトリ構造
```text
.
├── data
├── notebooks
├── scripts
├── src
│   ├── config
│   ├── __init__.py
│   ├── main.py
│   └── settings.py
├── poetry.lock
├── pyproject.toml
├── README.md
└── tests
```
