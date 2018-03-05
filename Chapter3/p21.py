#
# カテゴリの書かれた行を抽出せよ
#
from p20 import get_json

if __name__ == "__main__":
  answer = [line for line in get_json().split("\n") 
            if "Category" in line]
  print(answer) 
