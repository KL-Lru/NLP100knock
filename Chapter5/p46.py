#
# 動詞の格フレーム情報を抽出せよ
#

from p41 import getChunk

if __name__ == "__main__":
  for i in getChunk():
    for j in i:
      if j.morphs[0].pos == "動詞":
        src=[]
        srcmph=[]
        for k in j.srcs:
          if i[k].morphs[-1].pos == "助詞":
            src.append(i[k].morphs[-1].base)
            srcmph.append(i[k].morst())
        if src != []:
          print(j.morphs[0].base+"\t"+" ".join(src)+"\t"+" ".join(srcmph))
