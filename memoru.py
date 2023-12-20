#!/usr/bin/env python3

import argparse
import sys


def main():
    args = parse_args()
    # 以下に処理を書く


def parse_args():
    parser = argparse.ArgumentParser(description="memoru")
    # オプションを設定
    return parser.parse_args()


if __name__ == "__main__":
    sys.exit(main())
