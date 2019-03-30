# 基礎情報を辞書型に格納せよ(強調マークアップと内部リンクをテキストに変換)
from p25 import getBaseInfoText, convertDict
from p26 import removeMUStrength
from pprint import pprint
import re

def removeMUInnerLink(text):
    text_rem = re.sub("\[\[[^\[\]]*\|(.*?)\]\]",
                      '\\1',
                      text)
    text_rem = re.sub('\[\[(.*?)\]\]', '\\1', text_rem)
    return text_rem
# end def

if __name__ == "__main__":
    text = getBaseInfoText()
    text_rem = removeMUStrength(text)
    text_rem = removeMUInnerLink(text_rem)
    answer = convertDict(text_rem)
    pprint(answer)
