# 文を単語に分解し，各単語の文字数を先頭から出現順に並べたリストを作成せよ．

import re

if __name__ == "__main__":
    text = """
        Now I need a drink, alcoholic of course, 
        after the heavy lectures involving quantum mechanics.
        """
    words  = re.sub("[,\.]", " ", text)
    answer = [len(ti) for ti in words.split()]
    print(answer)