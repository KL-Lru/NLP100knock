# 単語の出現頻度の順位と頻度のグラフを描け

from p30 import getMecabData
import matplotlib.pyplot as plt
from math import log

if __name__ == "__main__":
    analysis = getMecabData()
    calc = {}
    for sentence in analysis:
        for word in sentence:
            if word["base"] in calc.keys():
                calc[word["base"]] += 1
            else:
                calc[word["base"]] = 1
    freqs_list = sorted(calc.values(), reverse = True)
    plt.plot(freqs_list, range(1,len(freqs_list)+1))
    plt.yscale('log') # 差が大きいのでlogスケールで
    plt.xlabel('Order')
    plt.ylabel('Frequency')
    plt.show()