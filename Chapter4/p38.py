# 
# 単語の出現頻度のヒストグラムを描け
# 

from p30 import get_mecab
from operator import itemgetter
from subprocess import Popen
from subprocess import PIPE
from pprint import pprint

analy=get_mecab()
calc={}
for i in analy:
  for j in i:
    if j["base"] in calc.keys():
      calc[j["base"]]+=1
    else:
      calc[j["base"]]=1
res ={}
for i in calc:
  if calc[i] in res.keys():
    res[calc[i]]+=1
  else:
    res[calc[i]]=1
res = sorted(res.items(),key=itemgetter(0),reverse=False)
res = "\n".join([str(x[0])+" "+str(x[1]) for x in res])

gncmd=b"""
set terminal xterm
set xrange[0:100]
plot '-' using 1:2 with boxes notitle
"""

plot=Popen([ "gnuplot", "-e"],stdin=PIPE,shell=True).stdin
plot.write(gncmd)
plot.write(res.encode())