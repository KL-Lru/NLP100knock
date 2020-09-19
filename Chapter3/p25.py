# 基礎情報を辞書型に格納せよ
from p20 import getUKText
from pprint import pprint
import regex
import re

def getBaseInfoText():
    # PCRE compile
    base_info_re = regex.compile(
        r"(?(DEFINE)(?P<RECS>{((?>[^{}]+|(?&RECS))*)})){{(?P<INFO>基礎情報(?:[^{}]*|(?&RECS))*)}}"
    )
    res = regex.search(base_info_re, getUKText())
    text = res.captures("INFO")[0]
    return text
# end def

def convertDict(text):
    dic = {}
    dict_re = re.compile(r"^(?P<key>[^=]*)=(?P<value>(?:.|\s)*)")
    for line in text.split("\n|")[1:]:
        res = re.search(dict_re, line)
        dic[res.group("key").strip()] = res.group("value").strip()
    return dic
# end def

if __name__ == "__main__":
    answer = convertDict(getBaseInfoText())
    pprint(answer)
    print(answer['国歌'])