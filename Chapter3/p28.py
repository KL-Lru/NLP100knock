# 基礎情報を辞書型に格納せよ(マークアップを可能な限り削除)
from p25 import getBaseInfoText, convertDict
from p26 import removeMarkUpStrength
from p27 import removeMarkUpInnerLink
from pprint import pprint
import re

def removeMarkUpOuterLink(text):
    text_rem = re.sub(r"(?<!\[)\[([^] ]*) ?([^]]*)\](?!\])",
                      lambda match: match.group(2) if match.group(2) else match.group(1),
                      text)
    return text_rem
# end def

def removeMarkUpHTMLTag(text):
    text_rem = re.sub(r"<[^>]*>",
                      "",
                      text)
    return text_rem
# end def

if __name__ == "__main__":
    text = getBaseInfoText()
    text = removeMarkUpStrength(text)
    text = removeMarkUpInnerLink(text)
    text = removeMarkUpOuterLink(text)
    text = removeMarkUpHTMLTag(text)
    answer = convertDict(text)
    pprint(answer)
