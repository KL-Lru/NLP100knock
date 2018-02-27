#
# 基礎情報を辞書型に格納せよ(強調マークアップをテキストに変換)
#
from p20 import getjson
from pprint import pprint
import re

#ans={re.sub("^(.*?) = .*","\\1",st,flags=re.DOTALL):re.sub(".* = (.*)","\\1",st,flags=re.DOTALL) for st in re.sub("'{2,}(.*?)'{2,}","\\1",re.sub(".*(\{\{基礎情報.*?\n)}}.*","\\1",getjson(),flags=re.DOTALL),flags=re.DOTALL).split("\n|")[1:]}
s=re.sub(".*(\{\{基礎情報.*?\n)}}.*","\\1",getjson(),flags=re.DOTALL)
s=re.sub("'{2,}(.*?)'{2,}","\\1",s,flags=re.DOTALL)
ans={re.sub("^(.*?) = .*","\\1",st,flags=re.DOTALL):re.sub(".* = (.*)","\\1",st,flags=re.DOTALL) for st in s.split("\n|")[1:]}
pprint(ans)