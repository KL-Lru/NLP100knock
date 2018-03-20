#!/usr/bin/env python3
#
# 基礎情報を辞書型に格納せよ(マークアップを可能な限り削除)
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
  text_rem = sub("<.*?>",
                 "",
                 text_rem,
                 flags=DOTALL)
  text_rem = sub("\*",
                 "",
                 text_rem,
                 flags=DOTALL)
  text_link_rem = []
  for tsr in text_rem.split("\n|")[1:]:
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
  text_template_rem = []
  for tsr in text_link_rem:
    #{{}}内の要らないとこを消す
    half_rem = []
    for ti in tsr.split("{{"): 
      if "}}" in ti:
        half_rem.append(sub("^.*\|",
                            "",
                            ti))
      else:
        half_rem.append(ti)
    half_rem = "{{".join(half_rem)
    no_template_text = sub("\{\{(.*?)\}\}",
                           "\\1",
                           half_rem)
    text_template_rem.append(no_template_text)
  answer = {}
  for line in text_template_rem:
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

