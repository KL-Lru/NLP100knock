#
# 基礎情報を辞書型に格納せよ(強調マークアップと内部リンクをテキストに変換)
#
from p20 import getjson
from pprint import pprint
import re

s=re.sub(".*(\{\{基礎情報.*?\n)}}.*","\\1",getjson(),flags=re.DOTALL)
s=re.sub("'{2,}(.*?)'{2,}","\\1",s,flags=re.DOTALL)
l=[]
for i in s.split("\n|")[1:]:
  l.append(re.sub("\[\[(.*?)]]","\\1","[[".join([re.sub("^.*\|","",j) if "]]" in j else j for j in i.split("[[")])))
ans={re.sub("^(.*?) = .*","\\1",st,flags=re.DOTALL):re.sub(".* = (.*)","\\1",st,flags=re.DOTALL) for st in l}
pprint(ans)