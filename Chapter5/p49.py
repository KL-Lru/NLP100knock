# 二回もgitにファイルを消されてキレているためコメントは知らない
# 
#

from p40 import Morph
from p41 import getChunks
from p43 import contain_noun
from copy import deepcopy

if __name__ == "__main__":
  for sentence in getChunks()[5:6]:
    nouns=[]
    for nc in range(len(sentence)):
      if contain_noun(sentence[nc]):
        nouns.append(nc)
    path=[]
    for i in nouns:
      l=[i]
      d=sentence[i]
      while(d.dst!=-1):
        l.append(d.dst)
        d=sentence[d.dst]
      path.append(l)

    for ni in range(len(nouns)):
      for nj in range(ni+1,len(nouns)):
        cross=min(set(path[ni]).intersection(set(path[nj])))

        ans=""
        if cross == nouns[nj]:
          d=deepcopy(sentence[ni])
          while(d.morphs and d.morphs[0].pos == "名詞"):
            del d.morphs[0]
          d.morphs.insert(0,Morph("X","","",""))
          while(d.dst != sentence[cross].dst):
            ans+=d.morphs2str()+"->"
            d=sentence[d.dst]
          ans+="Y"

        else:
          d=deepcopy(sentence[ni])
          while(d.morphs and d.morphs[0].pos == "名詞"):
            del d.morphs[0]
          d.morphs.insert(0,Morph("X","","",""))
          while(d.dst != cross):
            ans+=d.morphs2str()+"->"
            d=sentence[d.dst]
          ans+=d.morphs2str()+"|"
          d=deepcopy(sentence[nj])
          while(d.morphs and d.morphs[0].pos == "名詞"):
            del d.morphs[0]
          d.morphs.insert(0,Morph("Y","","",""))
          while(d.dst != cross):
            ans+=d.morphs2str()+"->"
            d=sentence[d.dst]
          ans+=d.morphs2str()+"|"
          d=sentence[d.dst]
          ans+=d.morphs2str()+"|"
        print(ans)         
      