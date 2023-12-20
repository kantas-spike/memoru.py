#!/usr/bin/env python3

import argparse
import datetime
import subprocess
import sys
import os


def main():
    args = parse_args()
    # 以下に処理を書く
    # ディレクトリがなければ作成
    output_dir = os.path.abspath(os.path.expanduser(args.output_dir))
    if not os.path.exists(output_dir):
        print(f"mkdir {output_dir}...")
        os.makedirs(output_dir)

    # メモファイルのパス作成
    now = datetime.datetime.now()
    memo_path = os.path.join(
        output_dir, f"{now.strftime('%Y%m%d_%H%M%S')}_{args.title}{args.extension}"
    )
    print(f"open {memo_path}...")
    subprocess.run(f"{args.editor_path} '{memo_path}'", shell=True, check=True)


def parse_args():
    parser = argparse.ArgumentParser("memoru", description="メモ用の空ファイルを作成し、vscodeで開く。")
    # オプションを設定
    DEFAULT_OUTPUT_DIR = "~/memo"
    DEFAULT_EXTENSION = ".md"
    DEFAULT_TITLE = "memo"
    DEFAULT_EDITOR = "code"

    parser.add_argument(
        "-o",
        "--output-dir",
        metavar="OUTPUT_DIR",
        help=f"メモファイル作成ディレクトリ.(デフォルト値: {DEFAULT_OUTPUT_DIR})",
        default=DEFAULT_OUTPUT_DIR,
    )

    parser.add_argument(
        "-e",
        "--extension",
        metavar="EXTENSION",
        help=f"メモファイルの拡張子. (デフォルト値: {DEFAULT_EXTENSION})",
        default=DEFAULT_EXTENSION,
    )

    parser.add_argument(
        "-t",
        "--title",
        metavar="TITLE",
        help=f"メモファイル名のサフィックスとなるタイトル. (デフォルト値: {DEFAULT_TITLE})",
        default=DEFAULT_TITLE,
    )

    parser.add_argument(
        "--editor-path",
        metavar="EDITOR_PATH",
        help=f"メモファイルを開くエディターのパス.(デフォルト値: {DEFAULT_EDITOR})",
        default=DEFAULT_EDITOR,
    )
    return parser.parse_args()


if __name__ == "__main__":
    sys.exit(main())
