# TSUKUBA-TAKEOUT-PROJECT

## 開発の仕方

### 開発環境

Pythonの環境には[poetry](https://python-poetry.org/)を使っています。

仮想環境は `.venv` 配下にあります。


### 開発を始める前に

プロジェクトルートディレクトリで下記コマンドを実行して依存ライブラリをインストールしてください。

```sh
$ poetry install
```

poetryの機能により、python仮想環境のシェルを立ち上げます。

```sh
$ poetry shell
```

今後はこのシェルの中で各コマンドを実行すると良いでしょう。

最初にデータベースの作成とマイグレーションを行います。


```sh
$ python manage.py makemigrations
$ python manage.py migrate
```

これで開発の準備は整います。

### 開発サーバの起動

以下のコマンドで開発サーバが起動します。

```sh
$ python manage.py runserver
```

その他のコマンド類に関してはdjangoのドキュメントを参考にしてください。


## Issue管理

このプロジェクトではIssueタスクチケットとして管理しています。

### Issueの作り方

issueにはテンプレートが用意されています。テンプレートに従って入力してください。

このプロジェクトのissueには、以下のようなラベルが用意されています。

![](./doc/img/issues.png)

接頭辞の数字順にラベルを付けると自然に分類される仕組みです。0は必要なときのみ付けてください。

issueを発行した際は、Projectに `PROJECT-KANBAN` を設定してください。設定することにより、[GitHub Projects](https://github.com/sudame/tsukuba-takeout/projects/1)で自動的にタスクが管理されます。