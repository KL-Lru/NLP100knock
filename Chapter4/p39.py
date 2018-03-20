#!/usr/bin/env python3
# 
# 単語の出現頻度の順位と頻度のグラフを描け
# 

from p30 import get_mecab
from operator import itemgetter
from subprocess import Popen
from subprocess import PIPE
from math import log

if __name__ == "__main__":
  analysis = get_mecab()
  calc = {}
  for ai in analysis:
    for aj in ai:
      if aj["base"] in calc.keys():
        calc[aj["base"]] += 1
      else:
        calc[aj["base"]] = 1
  calc = sorted(calc.items(),
                key = itemgetter(1),
                reverse = True)
  data = []
  for i in range(len(calc)):
    data.append([calc[i][1],i+1])
  data = "\n".join([str(log(x[0])) + " " + str(log(x[1])) for x in data])

  gncmd = """
  set terminal xterm
  set xrange[0:20]
  plot '-' using 1:2 with line notitle
  """

  plot = Popen([ "gnuplot", "-e"],
               stdin = PIPE,
               shell = True).stdin
  plot.write(gncmd.encode())
  plot.write(data.encode())