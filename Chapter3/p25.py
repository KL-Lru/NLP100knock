#
# 基礎情報を辞書型に格納せよ
#
from p20 import get_json
from re import sub
from re import DOTALL
from pprint import pprint

# re.DOTALL: .に\nを含ませる
# answer={sub("^(.*?) = .*","\\1",st,flags=DOTALL):sub(".* = (.*)","\\1",st,flags=re.DOTALL) for st in sub(".*(\{\{基礎情報.*?\n)}}.*","\\1",get_json(),flags=DOTALL).split("\n|")[1:]}
if __name__ == "__main__":
  text = sub(".*\{\{(基礎情報.*?)\n}}.*", 
             "\\1", 
             get_json(), 
             flags = DOTALL
             )
  answer={}
  for line in text.split("\n|")[1:]:
    answer[sub("^(.*?) = .*", 
           "\\1", 
           line, 
           flags = DOTALL
           )] = sub(".* = (.*)", 
                    "\\1", 
                    line, 
                    flags = DOTALL)
  pprint(answer)