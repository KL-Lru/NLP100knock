#
# カテゴリ名を抽出せよ
#
from p20 import getjson
import re

s=getjson().split("\n")
ans=[]
for st in s:
    if "Category" in st:
        ans.append(re.sub("\[.*:(.*).*]]","\\1",st))
print(ans)