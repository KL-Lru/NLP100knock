#!/usr/bin/env python3
#
# 参照されているファイルを全部抜き出せ
#
from p20 import get_json
from re import sub
from re import search
from pprint import pprint

if __name__ == "__main__":
  answer = []
  for line in get_json().split("\n"):
    if search("ファイル|File", line):
      name = sub(".*:(.*?)\|.*",
                 "\\1",
                line)
      answer.append(name)
  #内包表現を使う場合
  # answer = [sub(".*:(.*?)\|.*", "\\1", line) for line in get_json().split("\n") if search("ファイル|File", line)]
  pprint(answer)
