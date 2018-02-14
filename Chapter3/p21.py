#
# カテゴリの書かれた行を抽出せよ
#
from p20 import getjson

ans=[st for st in getjson().split("\n") if "Category" in st]
print(ans) 
