# 基礎情報を辞書型に格納せよ(マークアップを可能な限り削除)
from p25 import getBaseInfoText, convertDict
from p26 import removeMUStrength
from p27 import removeMUInnerLink
from pprint import pprint
import re

def removeMUOuterLink(text):
    # 内部リンクを先に消していないとバグの原因になります
    text_rem = re.sub("\[.*? (.*?)\]",
                      ' \\1',
                      text)
    return text_rem
# end def

def removeMUHTMLTag(text):
    text_rem = re.sub("<.*?>",
                      "",
                      text)
    return text_rem
# end def

def removeMUMiddleBracket(text):
    text_rem = re.sub("\{\{[^\{\}]*\|(.*?)\}\}",
                      '\\1',
                      text)
    text_rem = re.sub('\{\{(.*?)\}\}', '\\1', text_rem)
    return text_rem
# end def

if __name__ == "__main__":
    text = getBaseInfoText()
    text = removeMUStrength(text)
    text = removeMUInnerLink(text)
    text = removeMUOuterLink(text)
    text = removeMUHTMLTag(text)
    text = removeMUMiddleBracket(text)
    answer = convertDict(text)
    pprint(answer)
