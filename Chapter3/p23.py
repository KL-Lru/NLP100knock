#
# セクション名とそのレベルを表示せよ
#
from p20 import get_json
from re import sub
from re import match
from pprint import pprint

if __name__ == "__main__":
  answer=[[sub("=", "", line), int(line.count("=")/2 - 1)] 
          for line in get_json().split("\n") 
          if match("==", line)]
  pprint(answer)
