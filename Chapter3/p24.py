#
# 参照されているファイルを全部抜き出せ
#
from p20 import get_json
from re import sub
from re import search
from pprint import pprint

if __name__ == "__main__":
  answer = [sub(".*:(.*?)\|.*", "\\1", line) 
            for line in get_json().split("\n") 
            if search("ファイル|File", line)]
  print(answer)
