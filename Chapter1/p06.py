#
# 文字bi-gramの集合を，それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．
# さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．
#
from p05 import n_gram 
from pprint import pprint
from collections import OrderedDict


text1 = "paraparaparadise"
text2 = "paragraph"
x = set(n_gram(n = 2,
               mode = 'char',
               text = text1
               ))
y = set(n_gram(n = 2,
               mode = 'char',
               text = text2))
answer = OrderedDict() #確認用に入力した順序を保つ
answer["union"] = x.union(y)
answer["intersection"] = x.intersection(y)
answer["difference"] = x.symmetric_difference(y)
answer["se in x?"] = "se" in x
answer["se in y?"] = "se" in y
pprint(answer)
