#
# 動詞の格フレーム情報を抽出せよ
#

from p41 import getChunk

if __name__ == "__main__":
  for i in getChunk():
    for j in i:
      if j.morphs[0].pos == "動詞":
        mph=""
        for k in j.srcs:
          if i[k].morphs[-1].surface == "を" and i[k].morphs[-2].pos1 == "サ変接続":
            mph=i[k].morst()+j.morphs[0].base
        src=" ".join([i[x].morst() for x in j.srcs if i[x].morphs[-1].pos=="助詞" and x!=k])
        con=" ".join([i[x].morphs[-1].surface for x in j.srcs if i[x].morphs[-1].pos=="助詞" and x!=k])
        if mph != "" and src != '':
          print(mph+"\t"+con+"\t"+src)
