# 単語の出現頻度のヒストグラムを描け

from p30 import getMecabData
import matplotlib.pyplot as plt
import numpy as np
if __name__ == "__main__":
    analysis = getMecabData()
    calc = {}
    for sentence in analysis:
        for word in sentence:
            if word["base"] in calc.keys():
                calc[word["base"]] += 1
            else:
                calc[word["base"]] = 1
    freqs_list = list(calc.values())
    plt.hist(freqs_list, bins = 100, log = True) # 差が大きくて後半見えないのでlogスケールで
    plt.xlabel('Frequency')
    plt.ylabel('Count')
    plt.show()

