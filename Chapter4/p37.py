#!/usr/bin/env python3
# mecab neko.txt -E "" | cut -f1 | sort | uniq -c | sort -n -r | head -n 10 | awk '{print $2,$1}' | gnuplot -e "set terminal xterm; plot '-' using 0:2:xtic(1) with boxes notitle;"
# 単語の出現頻度を求め, 高い順から10個をグラフ化せよ
# 

from p30 import get_mecab
from operator import itemgetter
from subprocess import Popen
from subprocess import PIPE
from pprint import pprint

if __name__ == "__main__":
  analysis=get_mecab()
  calc={}
  for ai in analysis:
    for aj in ai:
      if aj["base"] in calc.keys():
        calc[aj["base"]] += 1
      else:
        calc[aj["base"]] = 1
  data = sorted(calc.items(),
               key = itemgetter(1),
               reverse = True)[0:10]
  data = "\n".join([str(x[0]) + " " + str(x[1]) for x in data])

  gncmd = """
  set terminal xterm
  plot '-' using 0:2:xtic(1) with boxes notitle
  """

  plot = Popen(["gnuplot", "-e"],
               stdin = PIPE,
               shell = True).stdin
  plot.write(gncmd.encode())
  plot.write(data.encode())

  #↑は通って↓でダメな理由がよくわからない…
  #echo=Popen(["echo",res],stdout=PIPE)
  #plot=Popen(["gnuplot", "-e", gncmd],stdin=echo.stdout,shell=True)