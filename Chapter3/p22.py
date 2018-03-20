#!/usr/bin/env python3
#
# カテゴリ名を抽出せよ
#
from p20 import get_json
from re import sub
from pprint import pprint

if __name__ == "__main__":
  answer = []
  for line in get_json().split("\n"):
    if "Category" in line:
      category=sub(".*\[Category:(.*).*]].*",
                   "\\1",
                  line)
      answer.append(category)
  # 内包表現を使う場合
  # answer = [sub(".*\[Category:(.*).*]].*", "\\1", line) for line in get_json().split("\n") if "Category" in line]
  pprint(answer)