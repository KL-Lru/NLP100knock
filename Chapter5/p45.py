#
# 動詞の格パターンを抽出せよ
#

from p41 import getChunk

if __name__ == "__main__":
  for i in getChunk():
    print("sentence:"+"".join([k.morst() for k in i]))
    for j in i:
      if j.morphs[0].pos == "動詞":
        src=[]
        for k in j.srcs:
          if i[k].morphs[-1].pos == "助詞":
            src.append(i[k].morphs[-1].base)
        if src != []:
          print(j.morphs[0].base+"\t"+" ".join(src))
