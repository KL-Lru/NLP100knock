# 基礎情報を辞書型に格納せよ(強調マークアップをテキストに変換)
from p25 import getBaseInfoText, convertDict
from pprint import pprint
import re

def removeMarkUpStrength(text):
    text_rem = re.sub(r"'{2,}(.*?)'{2,}",
                      r"\1",
                      text)
    return text_rem
# end def

if __name__ == "__main__":
    text = removeMarkUpStrength(getBaseInfoText())
    answer = convertDict(text)
    pprint(answer)
