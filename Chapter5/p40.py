#
# Morphクラスを作れ
#

from re import sub
from pprint import pprint

class Morph:
  def __init__(self, surf, base, pos, pos1):
    self.surface = surf
    self.base    = base
    self.pos     = pos
    self.pos1    = pos1

if __name__ == "__main__":
  f=open("neko.txt.cabocha","r")
  l=[]
  s=[]
  for i in f.readlines():
    i=sub("(\ |\t)", ",",i)
    a=i.split(",")
    if a[0] == "*":
      continue
    elif a[0] == "EOS\n":
      l.append(s)
      s=[]
    else:
      s.append(Morph(a[0],a[7],a[1],a[2]))
  print("".join([i.surface for i in l[2]]))