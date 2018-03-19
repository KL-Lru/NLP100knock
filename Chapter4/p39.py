# 
# 単語の出現頻度の順位と頻度のグラフを描け
# 

from p30 import get_mecab
from operator import itemgetter
from subprocess import Popen
from subprocess import PIPE
from pprint import pprint
from math import log

analy=get_mecab()
calc={}
for i in analy:
  for j in i:
    if j["base"] in calc.keys():
      calc[j["base"]]+=1
    else:
      calc[j["base"]]=1
calc = sorted(calc.items(),key=itemgetter(1),reverse=True)
#pprint(calc)
res=[]
for i in range(len(calc)):
  res.append([calc[i][1],i+1])
#pprint(res)
res = "\n".join([str(log(x[0]))+" "+str(log(x[1])) for x in res])

gncmd=b"""
set terminal xterm
set xrange[0:20]
plot '-' using 1:2 with line notitle
"""

plot=Popen([ "gnuplot", "-e"],stdin=PIPE,shell=True).stdin
plot.write(gncmd)
plot.write(res.encode())