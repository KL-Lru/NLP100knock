# 名詞から根までのパスを出力せよ

from p41 import getChunks

def print_path(sentence, src):
  print(sentence[src].morphs2str(), end = "")
  if sentence[src].dst != -1:
    print("->", end = "")
    print_path(sentence, sentence[src].dst)
  else:
    print("")
# end def print_path

if __name__ == "__main__":
  for sentence in getChunks():
    for cn in range(len(sentence)):
      if sentence[cn].morphs[0].pos == "名詞":
        print_path(sentence, cn)
