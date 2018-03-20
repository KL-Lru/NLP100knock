#!/usr/bin/env python3
#
# サ変接続の名詞を全て抽出せよ
#

from p30 import get_mecab

if __name__ == "__main__":
  analysis = get_mecab()
  answer = []
  for ai in analysis:
    for aj in ai:
      if aj["pos1"] == "サ変接続":
        answer.append(aj["base"])
  print(answer)