# 基礎情報を辞書型に格納せよ(強調マークアップをテキストに変換)
from p25 import getBaseInfoText, convertDict
from pprint import pprint
import re

# MU: Mark Up
def removeMUStrength(text):
    text_rem = re.sub("'{2,}(.*?)'{2,}",
                      "\\1",
                      text)
    return text_rem
# end def

if __name__ == "__main__":
    text = removeMUStrength(getBaseInfoText())
    answer = convertDict(text)
    pprint(answer)
