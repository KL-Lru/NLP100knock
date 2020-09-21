# 名詞間の係り受けパスの抽出

from p40 import Morph
from p41 import getChunks
from p43 import contain_noun
from copy import deepcopy

if __name__ == "__main__":
  for sentence in getChunks():
    # 名詞句集め
    nouns = []
    for nc in range(len(sentence)):
      if contain_noun(sentence[nc]):
        nouns.append(nc)
    
    # パス計算
    path = []
    for i in nouns:
      l = [i]
      d = sentence[i]
      while(d.dst != -1):
        l.append(d.dst)
        d = sentence[d.dst]
      path.append(l)

    for ni in range(len(nouns)):
      for nj in range(ni + 1,len(nouns)):
        # パスの交点はパスの積(集合)の最小値
        cross=min(set(path[ni]).intersection(set(path[nj])))

        answer = ""
        if cross == nouns[nj]:
          d = deepcopy(sentence[nouns[ni]]) # shallowコピーだと元の内容まで変えてしまうので
          while(d.morphs and d.morphs[0].pos == "名詞"):
            del d.morphs[0]
          d.morphs.insert(0, Morph("X", "", "", ""))
          while(d.dst != sentence[cross].dst):
            answer += d.morphs2str()+" -> "
            d = sentence[d.dst]
          answer += "Y"

        else:
          d = deepcopy(sentence[nouns[ni]])
          while(d.morphs and d.morphs[0].pos == "名詞"):
            del d.morphs[0]
          d.morphs.insert(0, Morph("X", "", "", ""))
          while(d.dst != cross):
            answer += d.morphs2str() + " -> "
            d = sentence[d.dst]
          answer += d.morphs2str() + " | "
          d = deepcopy(sentence[nouns[nj]])
          while(d.morphs and d.morphs[0].pos == "名詞"):
            del d.morphs[0]
          d.morphs.insert(0, Morph("Y", "", "", ""))
          while(d.dst != cross):
            answer += d.morphs2str() + " -> "
            d = sentence[d.dst]
          answer += d.morphs2str() + " | "
          d = sentence[d.dst]
          answer += d.morphs2str()
        print(answer)         
      