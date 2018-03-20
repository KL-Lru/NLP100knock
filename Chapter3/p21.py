#!/usr/bin/env python3
#
# カテゴリの書かれた行を抽出せよ
#
from p20 import get_json
from pprint import pprint

if __name__ == "__main__":
  answer = []
  for line in get_json().split("\n"):
    if "Category" in line:
      answer.append(line)
  # 内包表現を使う場合
  # answer = [line for line in get_json().split("\n") if "Category" in line]
  pprint(answer) 
