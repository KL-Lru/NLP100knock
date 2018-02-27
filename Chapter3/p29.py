#
# 国旗画像のurlを手に入れろ
#
from p20 import getjson
from pprint import pprint
import re
import requests

#スパゲッティになりつつある
#後で直そう

def search(data):
  ans=""
  if isinstance(data,dict):
    for i in data:
      if i=="url":
        ans+=data[i]
      else:
        ans+=search(data[i])
  elif isinstance(data,list):
    for i in data:
      ans+=search(i)
  return ans

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
di={re.sub("^(.*?) = .*","\\1",st,flags=re.DOTALL):re.sub(".* = (.*)","\\1",st,flags=re.DOTALL) for st in ll}
ans=search(requests.get("https://en.wikipedia.org/w/api.php",params={"action":"query","titles":"File:"+di['国旗画像'],"prop":"imageinfo","format":"json","iiprop":"url"}).json())
pprint(ans)