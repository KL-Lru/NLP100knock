# 単語の出現頻度の順位と頻度のグラフを描け

from p30 import getMecabData
from p35 import calcFrequency
import matplotlib.pyplot as plt
from math import log

if __name__ == "__main__":
    analysis = getMecabData()
    calc = {}
    freqs_list = [freq for (word,freq) in calcFrequency(analysis)]
    plt.plot(freqs_list, range(1,len(freqs_list)+1))
    plt.yscale('log')
    plt.xscale('log')
    plt.xlabel('Order')
    plt.ylabel('Frequency')
    plt.show()