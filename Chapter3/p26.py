#!/usr/bin/env python3
#
# 基礎情報を辞書型に格納せよ(強調マークアップをテキストに変換)
#
from p20 import get_json
from re import sub
from re import DOTALL
from pprint import pprint

if __name__ == "__main__":
  text = sub(".*(\{\{基礎情報.*?\n)}}.*", 
             "\\1", 
             get_json(), 
             flags = DOTALL)
  text_rem = sub("'{2,}(.*?)'{2,}", 
                 "\\1", 
                 text, 
                 flags = DOTALL)
  answer = {}
  for line in text_rem.split("\n|")[1:]:
    key = sub("^(.*?) = .*", 
               "\\1", 
               line, 
               flags = DOTALL)
    value = sub(".* = (.*)", 
                "\\1", 
                line, 
                flags = DOTALL)
    answer[key] = value
  pprint(answer)