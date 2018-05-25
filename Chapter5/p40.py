#!/usr/bin/env python3
#
# Morphクラスを作れ
#

from re import sub

class Morph:
  def __init__(self, surf, base, pos, pos1):
    self.surface = surf
    self.base    = base
    self.pos     = pos
    self.pos1    = pos1
#end Morph

def getMorphs():
  file = open("neko.txt.cabocha","r")
  list_sentence = []
  sentence = []
  for fi in file.readlines():
    fi = sub("(\ |\t)", ",",fi)
    elements = fi.split(",")
    if elements[0] == "*":
      continue
    elif elements[0] == "EOS\n":
      list_sentence.append(sentence)
      sentence = []
    else:
      sentence.append(Morph(surf = elements[0],  
                            base = elements[7],
                            pos  = elements[1],
                            pos1 = elements[2]))
  file.close()
  return list_sentence
#end def getMorphs

if __name__ == "__main__":
  list_sentence = getMorphs()
  answer = "".join([i.surface for i in list_sentence[2]])
  print(answer)
