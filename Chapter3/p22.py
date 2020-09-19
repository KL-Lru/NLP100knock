# カテゴリ名を抽出せよ
from p20 import getUKText
from pprint import pprint
import re

if __name__ == "__main__":
    answer = []
    for line in getUKText().split("\n"):
        res = re.search(r"\[Category:([^]]*)", line)
        if res:
            answer.append(res.group(1))
    pprint(answer)
