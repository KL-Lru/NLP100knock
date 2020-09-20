# 「猫」と共起頻度の単語の出現頻度を求め, 高い順から10個をグラフ化せよ

from p30 import getMecabData
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams['font.family'] = 'Myrica M'

if __name__ == "__main__":
    analysis = getMecabData()
    calc = {}
    for sentence in analysis:
        neko_flag = False
        for word in sentence:
            if word["base"] == "猫":
                neko_flag = True
        if not neko_flag:
            continue
        for word in sentence:
            if word["base"] == "猫":
                continue
            if word["base"] in calc.keys():
                calc[word["base"]] += 1
            else:
                calc[word["base"]] = 1
    freqs_list = sorted(calc.items(),
                        key = lambda x:x[1],
                        reverse=True)
    data = freqs_list[0:10]
    left   = [x[0] for x in data]
    height = [x[1] for x in data]
    plt.bar(left, height)
    plt.show()
