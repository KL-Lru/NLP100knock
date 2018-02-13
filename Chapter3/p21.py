#
# カテゴリの書かれた行を抽出せよ
#
from p20 import getjson

s=getjson().split("\n")
ans=[]
for st in s:
    if "Category" in st:
        ans.append(st)
print(ans) 
