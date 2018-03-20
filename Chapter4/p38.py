#!/usr/bin/env python3
# 
# 単語の出現頻度のヒストグラムを描け
# 

from p30 import get_mecab
from operator import itemgetter
from subprocess import Popen
from subprocess import PIPE
from pprint import pprint

if __name__ == "__main__":
  analysis = get_mecab()
  calc = {}
  for ai in analysis:
    for aj in ai:
      if aj["base"] in calc.keys():
        calc[aj["base"]] += 1
      else:
        calc[aj["base"]] = 1
  cnt = {}
  for ci in calc:
    if calc[ci] in cnt.keys():
      cnt[calc[ci]]+=1
    else:
      cnt[calc[ci]]=1
  data = sorted(cnt.items(),
                key = itemgetter(0),
                reverse = False)
  data = "\n".join([str(x[0]) + " " + str(x[1]) for x in data])

  gncmd = """
  set terminal xterm
  set xrange[0:100]
  plot '-' using 1:2 with boxes notitle
  """

  plot = Popen(["gnuplot", "-e"],
               stdin = PIPE,
               shell = True).stdin
  plot.write(gncmd.encode())
  plot.write(data.encode())