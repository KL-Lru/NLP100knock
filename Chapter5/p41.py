#
# Chunkクラスを作れ
#

from re import sub
from pprint import pprint
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

  def stout(self):
    st = "".join([i.surface for i in self.morphs])
    st += " " + str(self.dst)
    st += " " + str(self.srcs)
    return st

  def morst(self):
    return "".join([i.surface if i.surface!="。" and i.surface!="、" else "" for i in self.morphs])
#end Chunk

def getChunk():
  file = open("neko.txt.cabocha", "r")
  list_sent = []
  sentence = []
  chu = None
  for fi in file.readlines():
    fi = sub("(\ |\t)", ",",fi)
    ele = fi.split(",")
    if ele[0] == "*":
      if(chu is not None):
        sentence.append(chu) 
      dst = int(sub("^(.*)D","\\1",ele[2]))
      chu = Chunk(dst)
    elif ele[0] == "EOS\n":
      if(chu is not None):
        sentence.append(chu)
        chu = None
      if sentence == []:
        continue
      for j in range(len(sentence)):
        if sentence[j].dst != -1:
          sentence[sentence[j].dst].add_src(j)
      list_sent.append(sentence)
      sentence = []
    else:
      chu.add_morph(Morph(surf = ele[0],
                          base = ele[7],
                          pos  = ele[1],
                          pos1 = ele[2]))
  file.close()
  return list_sent
#end getChunk

if __name__ == "__main__":
  list_sent = getChunk()
  answer = "\n".join([i.stout() for i in list_sent[8]])
  print(answer)
