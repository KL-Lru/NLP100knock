#
# 係り受け関係を示せ
#

from re import sub
from pprint import pprint
from p41 import getChunk

if __name__ == "__main__":
  list_sent = getChunk()
  for sent in list_sent:
    for chunk in sent:
      if chunk.dst != -1:
        print(chunk.morst() + '\t' + sent[chunk.dst].morst())
