#
# カテゴリ名を抽出せよ
#
from p20 import get_json
from re import sub

if __name__ == "__main__":
  answer = [sub(".*\[Category:(.*).*]].*", "\\1", line) 
            for line in get_json().split("\n") 
            if "Category" in line]
  print(answer)