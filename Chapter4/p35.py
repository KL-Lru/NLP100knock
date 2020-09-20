# 単語の出現頻度を求め, 高い順に並べよ

from p30 import getMecabData
from pprint import pprint

def calcFrequency(analyzed_text):
    calc = {}
    for sentence in analyzed_text:
        for word in sentence:
            if word["base"] in calc.keys():
                calc[word["base"]] += 1
            else:
                calc[word["base"]] = 1
    freqs_list = sorted(calc.items(),
                        key = lambda x:x[1],
                        reverse=True)
    return freqs_list
# end def

if __name__ == "__main__":
    analysis = getMecabData()
    freqs_list = calcFrequency(analysis)
    answer = [word for (word, freq) in freqs_list]
    pprint(answer)
