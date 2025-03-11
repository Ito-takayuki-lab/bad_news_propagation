# 環境構築手順

## 必要な環境
このプロジェクトは、`requirements.txt` に記載されたライブラリに依存しています。

### Python のバージョン
使用する Python のバージョンは `requirements.txt` の内容に準拠してください。

## インストール手順
1. **リポジトリをクローン**
    ```sh
    git clone <repository_url>
    ```

2. **仮想環境の作成（使用するPCの環境(Conda、uv等)に従ってください）、以下は一例です** 
    ```sh
    conda create -n [仮想環境名]
    ```

3. **依存関係のインストール**
    ```sh
    pip install -r requirements.txt
    ```

## 実行方法

実行するファイルは、検証の場合は`main.py`、提案手法を施す場合は`agent_update.py`のproposed_promptを変更し、 `main_update.py`を実行してください。
以下のコマンドでメインスクリプトを実行できます。

1. 直列型
```sh
cd experiment1
# 検証の場合
python main.py
# 提案手法の場合
python main_agent.py
```
2. 多重対話型
```sh
cd experiment2
# 検証の場合
python main.py
# 提案手法の場合
python main_agent.py
```
3. 集団型
```sh
cd experiment3
# 検証の場合
python main.py
# 提案手法の場合
python main_agent.py
```
