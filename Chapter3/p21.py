# カテゴリの書かれた行を抽出せよ
from p20 import getUKText
import re
from pprint import pprint

if __name__ == "__main__":
    answer = [line for line in getUKText().split("\n") if re.search(r"\[\[Category:[^]]*]]", line)]
    pprint(answer)
