#
# カテゴリ名を抽出せよ
#
from p20 import getjson
import re

ans=[re.sub(".*\[Category:(.*).*]].*","\\1",st) for st in getjson().split("\n") if "Category" in st]
print(ans)