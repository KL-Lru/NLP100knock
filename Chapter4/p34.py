#!/usr/bin/env python3
#
# 「AのB」となる名詞句を全て抽出せよ
#

from p30 import get_mecab

if __name__ == "__main__":
  analysis = get_mecab()
  answer = []
  for ai in analysis:
    for j in range(len(ai)-2):
      if ai[j]["pos"] == "名詞" \
        and ai[j+1]["surface"] == "の" \
        and ai[j+2]["pos"] == "名詞":
        answer.append(ai[j]["surface"] \
                  + ai[j+1]["surface"] \
                  + ai[j+2]["surface"])
  print(answer)