#!/usr/bin/env python3
# mecab -F "%m,%H\n" neko.txt > neko.txt.mecab
# ↑これでmecabファイルを作ると区切りが全てカンマになるので楽になる
# 
# 形態素解析結果を読み込め
#

from pprint import pprint

def get_mecab():
  file=open("neko.txt.mecab","r")
  res = []
  sentence = []
  for line in file.readlines():
    if line == "EOS\n":
      res.append(sentence)
      sentence = []
      continue
    analysis = line[:-1].split(",") #改行記号抜き
    info = {"surface":analysis[0],
            "base":analysis[7],
            "pos":analysis[1],
            "pos1":analysis[2]}
    sentence.append(info)
  return res

if __name__ == "__main__":
  answer = get_mecab()
  pprint(answer)