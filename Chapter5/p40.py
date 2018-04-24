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

def getMorphs():
  file = open("neko.txt.cabocha","r")
  list_sent = []
  sentence = []
  for fi in file.readlines():
    fi = sub("(\ |\t)", ",",fi)
    ele = fi.split(",")
    if ele[0] == "*":
      continue
    elif ele[0] == "EOS\n":
      list_sent.append(sentence)
      sentence = []
    else:
      sentence.append(Morph(surf = ele[0],  
                            base = ele[7],
                            pos  = ele[1],
                            pos1 = ele[2]))
  file.close()
  return list_sent  

if __name__ == "__main__":
  list_sent = getMorphs()
  answer = "".join([i.surface for i in list_sent[2]])
  print(answer)
