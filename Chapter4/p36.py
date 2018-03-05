# mecab neko.txt -E "" | cut -f1 | sort | uniq -c | sort -n -r 
# 単語の出現頻度を求め, 高い順に並べよ
# 

from p30 import get_mecab
from operator import itemgetter
from collections import OrderedDict
from pprint import pprint

analy=get_mecab()
calc={}
for i in analy:
  for j in i:
    if j["base"] in calc.keys():
      calc[j["base"]]+=1
    else:
      calc[j["base"]]=1
ans = OrderedDict(sorted(calc.items(),key=itemgetter(1),reverse=True))
pprint(ans)