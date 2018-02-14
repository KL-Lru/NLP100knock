#
# セクション名とそのレベルを表示せよ
#
from p20 import getjson
import re
from pprint import pprint

ans=[[re.sub("=","",st),int(st.count("=")/2-1)] for st in getjson().split("\n") if re.match("==",st)]
pprint(ans)
