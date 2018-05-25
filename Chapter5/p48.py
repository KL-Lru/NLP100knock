#
# 名詞から根までのパスを出力せよ
#

from p41 import getChunk

def print_path(sentence, src):
  print(sentence[src].morst(),end="")
  if sentence[src].dst!=-1:
    print("->",end="")
    print_path(sentence,sentence[src].dst)
  else:
    print("")
#end def

if __name__ == "__main__":
  for i = getChunk():
    for j in range(len(i)):
      if i[j].morphs[0].pos == "名詞":
        print_path(i,j)
