#!/usr/bin/env python3
#
# Chunkクラスを作れ
#

from re import sub
from p40 import Morph


class Chunk:
  def __init__(self, dst):
    self.morphs = []
    self.dst    = dst
    self.srcs   = []

  def add_src(self, src):
    self.srcs.append(src)

  def add_morph(self, morph):
    self.morphs.append(morph)

  #出力用関数
  def str_out(self):
    st = "".join([i.surface for i in self.morphs])
    st += " " + str(self.dst)
    st += " " + str(self.srcs)
    return st

  def morphs2str(self):
    return "".join([i.surface 
                    for i in self.morphs
                    if i.surface != "。" and i.surface != "、"])
#end def Chunk

def getChunks():
  file = open("neko.txt.cabocha", "r")
  list_sentence = []
  sentence = []
  chunks = None
  for fi in file.readlines():
    fi = sub("(\ |\t)", ",",fi)
    elements = fi.split(",")
    # next chunk
    if elements[0] == "*":
      if chunks is not None:
        sentence.append(chunks) 
      dst = int(sub("^(.*)D","\\1",elements[2]))
      chunks = Chunk(dst)
    #end sentence
    elif elements[0] == "EOS\n":
      if chunks is not None:
        sentence.append(chunks)
        chunks = None
      if sentence == []:
        continue
      for j in range(len(sentence)):
        if sentence[j].dst != -1:
          sentence[sentence[j].dst].add_src(j)
      list_sentence.append(sentence)
      sentence = []
    #add morph
    else:
      chunks.add_morph(Morph(surf = elements[0],
                             base = elements[7],
                             pos  = elements[1],
                             pos1 = elements[2]))
  file.close()
  return list_sentence
#end def getChunks

if __name__ == "__main__":
  list_sentence = getChunks()()
  answer = "\n".join([i.str_out() for i in list_sentence[8]])
  print(answer)
