# 参照されているファイルを全部抜き出せ
from p20 import getUKText
from pprint import pprint
import re

if __name__ == "__main__":
    answer = []
    for line in getUKText().split("\n"):
        res = re.search("(?:ファイル|File):(.*?)\|", line)
        if res:
            answer.append(res.group(1))
    pprint(answer)
