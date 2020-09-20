# 単語の出現頻度のヒストグラムを描け

from p30 import getMecabData
from p35 import calcFrequency
import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
    analysis = getMecabData()
    freqs_list = [freq for (word,freq) in calcFrequency(analysis)]
    plt.hist(freqs_list, bins = 100, log = True)
    plt.xlabel('Frequency')
    plt.ylabel('Count')
    plt.show()

