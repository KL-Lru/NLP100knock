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

  def out(self):
    for i in self.morphs:
      print(i.surface,end="")
    print("",self.dst,self.srcs)

  def fout(self):
    for i in self.morphs:
      i.fout()
  
  def morst(self):
    return "".join([i.surst() for i in self.morphs])

def getChunk():
  f=open("neko.txt.cabocha","r")
  l=[]
  s=[]
  c=None
  for i in f.readlines():
    i=sub("(\ |\t)", ",",i)
    a=i.split(",")
    if a[0] == "*":
      if(c is not None):
        s.append(c) 
      d=int(sub("^(.*)D","\\1",a[2]))
      c=Chunk(d)
    elif a[0] == "EOS\n":
      if(c is not None):
        s.append(c)
        c=None
      if s == []:
        continue
      for j in range(len(s)):
        if s[j].dst != -1:
          s[s[j].dst].add_src(j)
      l.append(s)
      s=[]
    else:
      c.add_morph(Morph(a[0],a[7],a[1],a[2]))
  return l

if __name__ == "__main__":
  l=getChunk()
  for i in l[8]:
    i.out() 
