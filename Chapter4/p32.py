#!/usr/bin/env python3
#
# 動詞の原形を全て抽出せよ
#

from p30 import get_mecab

if __name__ == "__main__":
  analysis = get_mecab()
  answer = []
  for ai in analysis:
    for aj in ai:
      if aj["pos"] == "動詞":
        answer.append(aj["base"])
  print(answer)