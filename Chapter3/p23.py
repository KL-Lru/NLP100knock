# セクション名とそのレベルを表示せよ
from p20 import getUKText
from pprint import pprint
import re

if __name__ == "__main__":
    answer = [ [line.replace("=", "").strip(), int(line.count("=")/2 - 1)] 
               for line in getUKText().split("\n") 
               if re.match(r"==", line)]
    pprint(answer)
