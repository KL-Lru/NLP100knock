#!/usr/bin/env python3
#
# 国旗画像のurlを手に入れろ
#
from p20 import get_json
from re import sub
from re import DOTALL
from requests import get as req_get
from pprint import pprint

def search_url(data):
  res = ""
  if isinstance(data, dict):
    for di in data:
      if di == "url":
        res += data[di]
      else:
        res += search_url(data[di])
  elif isinstance(data, list):
    for di in data:
      res += search_url(di)
  return res

if __name__ == "__main__":
  text = sub(".*(\{\{基礎情報.*?\n)}}.*", 
             "\\1", 
             get_json(), 
             flags = DOTALL)
  # linkがファイル名になっていればよいのでlinkのみ削除
  text_link_rem = []
  for tsr in text.split("\n|")[1:]:
    #[[]]内の要らないとこを消す
    half_rem = []
    for ti in tsr.split("[["): 
      if "]]" in ti:
        half_rem.append(sub("^.*\|",
                            "",
                            ti))
      else:
        half_rem.append(ti)
    half_rem = "[[".join(half_rem)
    no_link_text = sub("\[\[(.*?)]]",
                       "\\1",
                       half_rem)
    text_link_rem.append(no_link_text)
  info_dic = {}
  for line in text_link_rem:
    key = sub("^(.*?) = .*", 
               "\\1", 
               line, 
               flags = DOTALL)
    value = sub(".* = (.*)", 
                "\\1", 
                line, 
                flags = DOTALL)
    info_dic[key] = value
  res = req_get("https://en.wikipedia.org/w/api.php",
                params = {"action":"query",
                          "titles":"File:" + info_dic['国旗画像'],
                          "prop":"imageinfo",
                          "format":"json",
                          "iiprop":"url"})
  answer = search_url(res.json())
  pprint(answer)

