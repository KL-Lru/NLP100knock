#!/usr/bin/env python3
#
# 機能動詞構文のマイニング
#

from p41 import getChunks

if __name__ == "__main__":
  for sentence in getChunks():
    for chunk in sentence:
      if chunk.morphs[0].pos == "動詞":
        predicate = ""
        for si in chunk.srcs:
          if sentence[si].morphs[-1].surface == "を" and sentence[si].morphs[-2].pos1 == "サ変接続":
            predicate = sentence[si].morphs2str() + chunk.morphs[0].base
        src = " ".join([x.morphs2str() for x in sorted([sentence[x] 
                                               for x in chunk.srcs 
                                               if sentence[x].morphs[-1].pos == "助詞" and x != si],
                                       key = lambda x : x.morphs[-1].surface)])
        con = " ".join(sorted([sentence[x].morphs[-1].surface 
                               for x in chunk.srcs 
                               if sentence[x].morphs[-1].pos == "助詞" and x != si]))
        if predicate != "" and src != '':
          print(predicate \
                + "\t" + con \
                + "\t" + src)
