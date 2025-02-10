# BABELデータセットの可視化
BABELデータセットをLLMを用いて構築し、可視化を行うためのリポジトリ

## 環境構築
プロジェクトディレクトリ以下で
```
poetry install
```
```
poetry shell
```

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
