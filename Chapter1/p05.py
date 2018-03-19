#!/usr/bin/env python3
#
# 与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．
# この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．
#

def n_gram(n, mode, text):
  res = []
  res_unic = []
  if mode == 'word':
    words = text.split()
    for i in range(len(words)-n+1):
      res.append(" ".join(words[i:i+n:1]))
  elif mode == 'char':
    chars = text.replace(" ", "")
    for i in range(len(chars)-n+1):
      res.append(chars[i:i+n:1])
  for ri in res:
    if ri not in res_unic:
      res_unic.append(ri)
  return res_unic
#end def

if __name__ == "__main__":
  answer = n_gram(n = 2, 
                  mode = 'word', 
                  text = "I am an NLPer")
  print(answer)
  answer = n_gram(n = 2, 
                  mode = 'char', 
                  text = "I am an NLPer")
  print(answer)
