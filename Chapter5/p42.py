# 係り受け関係を示せ

from p41 import getChunks

if __name__ == "__main__":
  for sentence in getChunks():
    for chunk in sentence:
      if chunk.dst != -1:
        print(chunk.morphs2str() \
              + '\t' \
              + sentence[chunk.dst].morphs2str())
