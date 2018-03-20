#!/usr/bin/env python3
#
# 名詞の連接を最長一致で全て抽出せよ
#

from p30 import get_mecab

if __name__ == "__main__":
  analysis = get_mecab()
  answer = []
  for ai in analysis:
    noun = ""
    cnt = 0
    for j in range(len(ai)):
      if ai[j]["pos"] == "名詞":
        noun = noun + ai[j]["surface"]
        cnt += 1
      else:
        if cnt >= 2:
          answer.append(noun)
        cnt = 0
        noun = ""
  print(answer)