#
# 参照されているファイルを全部抜き出せ
#
from p20 import getjson
from pprint import pprint
import re

ans=[re.sub(".*:(.*?)\|.*","\\1",st) for st in getjson().split("\n") if re.search("ファイル|File",st)]
print(ans)
