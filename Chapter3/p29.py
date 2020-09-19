# 国旗画像のurlを手に入れろ
from p20 import getUKText
from p25 import getBaseInfoText, convertDict
from p27 import removeMarkUpInnerLink
from pprint import pprint
import requests
import re


def findURL(data):
    # jsonデータからURLを再帰的に見つけるまで走破する
    res = ""
    if isinstance(data, dict):
        for dkey, dval in data.items():
            if dkey == "url":
                res += dval
            else:
                res += findURL(dval)
    elif isinstance(data, list):
        for di in data:
            res += findURL(di)
    return res
# end def

if __name__ == "__main__":
    text = getBaseInfoText()

    # linkがファイル名になっていればよいのでlinkのみマークアップを削除
    text = removeMarkUpInnerLink(text)
    info_dic = convertDict(text)
    res = requests.get("https://en.wikipedia.org/w/api.php",
                       params={"action": "query",
                               "titles": "File:" + info_dic['国旗画像'],
                               "prop": "imageinfo",
                               "format": "json",
                               "iiprop": "url"})
    answer = findURL(res.json())
    pprint(answer)
