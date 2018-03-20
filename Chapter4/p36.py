#!/usr/bin/env python3
# mecab neko.txt -E "" | cut -f1 | sort | uniq -c | sort -n -r 
# 単語の出現頻度を求め, 高い順に並べよ
# 

from p30 import get_mecab
from operator import itemgetter
from collections import OrderedDict
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
  answer = OrderedDict(sorted(calc.items(),
                              key = itemgetter(1),
                              reverse = True))
  pprint(answer)