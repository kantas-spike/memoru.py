# memoru.py

メモ用の空ファイルを作成し、vscodeで開く。

vscodeからコマンドランチャー経由で実行することを想定。

## 使い方

以下を実行すると、`~/memo/{年月日_時分秒}_{タイトル}.md`に空のファイル作成し、`vscode`で開く。

```shell
~/bin/memoru
```

詳細は以下を参照

```shell
usage: memoru [-h] [-o OUTPUT_DIR] [-e EXTENSION] [-t TITLE] [--editor-path EDITOR_PATH]

メモ用の空ファイルを作成し、vscodeで開く。

options:
  -h, --help            show this help message and exit
  -o OUTPUT_DIR, --output-dir OUTPUT_DIR
                        メモファイル作成ディレクトリ.(デフォルト値: ~/memo)
  -e EXTENSION, --extension EXTENSION
                        メモファイルの拡張子. (デフォルト値: .md)
  -t TITLE, --title TITLE
                        メモファイル名のサフィックスとなるタイトル. (デフォルト値: memo)
  --editor-path EDITOR_PATH
                        メモファイルを開くエディターのパス.(デフォルト値: code)
```
