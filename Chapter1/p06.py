# 文字bi-gramの集合を，それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．
# さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．

from p05         import n_gram 
from pprint      import pprint

if __name__ == '__main__':
    text1 = 'paraparaparadise'
    text2 = 'paragraph'
    x = set(n_gram(n        = 2,
                   sequence = text1))
    y = set(n_gram(n        = 2,
                   sequence = text2))
    answer = {
        'union'       : x.union(y),
        'intersection': x.intersection(y),
        'difference'  : x.symmetric_difference(y),
        '"se" in x'   : 'se' in x,
        '"se" in y'   : 'se' in y,
    }
    pprint(answer)
