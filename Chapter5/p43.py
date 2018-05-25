#!/usr/bin/env python3
#
# 名詞を含む文節⇒動詞を含む文節を抽出
#
from p41 import getChunks

def contain_noun(chunk):
  for morph in chunk.morphs:
    if morph.pos == "名詞":
        return True
  return False
#end def contain_noun

def contain_verb(chunk):
  for morph in chunk.morphs:
    if morph.pos == "動詞":
        return True
  return False
#end def contain verb

if __name__ == "__main__":
  for sentence in getChunks():
    for chunk in sentence:
      if contain_noun(chunk) and contain_verb(sentence[chunk.dst]):
        print(chunk.morphs2str() \
              + '\t' \
              + sentence[chunk.dst].morphs2str())