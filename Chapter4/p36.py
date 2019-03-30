# 単語の出現頻度を求め, 高い順に並べよ

from p30 import getMecabData
from pprint import pprint

if __name__ == "__main__":
    analysis = getMecabData()
    calc = {}
    for sentence in analysis:
        for word in sentence:
            if word["base"] in calc.keys():
                calc[word["base"]] += 1
            else:
                calc[word["base"]] = 1
    freqs_list = sorted(calc.items(),
                        key = lambda x:x[1],
                        reverse=True)
    answer = [word for (word, freq) in freqs_list]
    pprint(answer)
