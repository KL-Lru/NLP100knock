#
# 基礎情報を辞書型に格納せよ(強調マークアップをテキストに変換)
#
from p20 import get_json
from re import sub
from re import DOTALL
from pprint import pprint

if __name__ == "__main__":
  text = sub(".*(\{\{基礎情報.*?\n)}}.*", 
             "\\1", 
             get_json(), 
             flags = DOTALL
             )
  text = sub("'{2,}(.*?)'{2,}", 
             "\\1", 
             text, 
             flags = DOTALL
             )
  ans={re.sub("^(.*?) = .*","\\1",st,flags=re.DOTALL):re.sub(".* = (.*)","\\1",st,flags=re.DOTALL) for st in s.split("\n|")[1:]}
  pprint(ans)