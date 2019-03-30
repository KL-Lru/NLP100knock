# 基礎情報を辞書型に格納せよ
from p20 import getUKText
from pprint import pprint
import re

# re.DOTALL: .に\nを含ませる
def getBaseInfoText():
    res = re.search("\{\{(基礎情報.*?)\n}}",
                    getUKText(),
                    flags=re.DOTALL)
    text = res.group(1)
    return text
# end def

def convertDict(text):
    dic = {}
    for line in text.split("\n|")[1:]:
        res = re.search('^(?P<key>.*?) = (?P<value>.*)',
                        line,
                        flags=re.DOTALL)
        dic[res.group('key')] = res.group('value')
    return dic
# end def

if __name__ == "__main__":
    answer = convertDict(getBaseInfoText())
    pprint(answer)
