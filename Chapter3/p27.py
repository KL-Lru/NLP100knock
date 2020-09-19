# 基礎情報を辞書型に格納せよ(強調マークアップと内部リンクをテキストに変換)
from p25 import getBaseInfoText, convertDict
from p26 import removeMarkUpStrength
from pprint import pprint
import re

def removeMarkUpInnerLink(text):
    text_rem = re.sub(r"\[\[(?:[^]\|]*\|)?([^]]*?)]]",
                      r"\1",
                      text)
    return text_rem
# end def

if __name__ == "__main__":
    text = getBaseInfoText()
    text_rem = removeMarkUpStrength(text)
    text_rem = removeMarkUpInnerLink(text_rem)
    answer = convertDict(text_rem)
    pprint(answer)
