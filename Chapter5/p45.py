# 動詞の格パターンを抽出せよ

from p41 import getChunks

if __name__ == "__main__":
  for sentence in getChunks():
    for chunk in sentence:
      if chunk.morphs[0].pos == "動詞":
        src=[]
        for si in chunk.srcs:
          if sentence[si].morphs[-1].pos == "助詞":
            src.append(sentence[si].morphs[-1].base)
        if src != []:
          print(chunk.morphs[0].base \
                + "\t" \
                + " ".join(sorted(src)))
