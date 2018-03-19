# mecab neko.txt -E "" | cut -f1 | sort | uniq -c | sort -n -r | head -n 10 | awk '{print $2,$1}' | gnuplot -e "set terminal xterm; plot '-' using 0:2:xtic(1) with boxes notitle;"
# 単語の出現頻度を求め, 高い順から10個をグラフ化せよ
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
res = sorted(calc.items(),key=itemgetter(1),reverse=True)[0:10]
res = "\n".join([str(x[0])+" "+str(x[1]) for x in res])

gncmd=b"""
set terminal xterm
plot '-' using 0:2:xtic(1) with boxes notitle
"""

plot=Popen([ "gnuplot", "-e"],stdin=PIPE,shell=True).stdin
plot.write(gncmd)
plot.write(res.encode())

#↑は通って↓でダメな理由がよくわからない…
#echo=Popen(["echo",res],stdout=PIPE)
#plot=Popen(["gnuplot", "-e", gncmd],stdin=echo.stdout,shell=True)