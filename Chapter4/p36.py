# 単語の出現頻度を求め, 高い順から10個をグラフ化せよ

from p30 import getMecabData
from p35 import calcFrequency
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams['font.family'] = 'Myrica M'

if __name__ == "__main__":
    analysis = getMecabData()
    freqs_list = calcFrequency(analysis)
    data = freqs_list[:10]
    left   = [x[0] for x in data]
    height = [x[1] for x in data]
    plt.bar(left, height)
    plt.show()
