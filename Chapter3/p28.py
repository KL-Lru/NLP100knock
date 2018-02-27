#
# 基礎情報を辞書型に格納せよ(マークアップを可能な限り削除)
#
from p20 import getjson
from pprint import pprint
import re

s=re.sub(".*(\{\{基礎情報.*?\n)}}.*","\\1",getjson(),flags=re.DOTALL)
s=re.sub("'{2,}(.*?)'{2,}","\\1",s,flags=re.DOTALL)
s=re.sub("<.*?>","",s,flags=re.DOTALL)
s=re.sub("\*","",s,flags=re.DOTALL)
l=[]
for i in s.split("\n|")[1:]:
  l.append(re.sub("\[\[(.*?)]]","\\1","[[".join([re.sub("^.*\|","",j) if "]]" in j else j for j in i.split("[[")])))
ll=[]
for i in l:
  ll.append(re.sub("\{\{(.*?)\}\}","\\1","{{".join([re.sub("^.*\|","",j) if "}}" in j else j for j in i.split("{{")])))
ans={re.sub("^(.*?) = .*","\\1",st,flags=re.DOTALL):re.sub(".* = (.*)","\\1",st,flags=re.DOTALL) for st in ll}
pprint(ans)