# 与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．
# この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．

def n_gram(n, sequence):
    grams = []
    for idx in range(len(sequence) - n + 1):
        gram = ''.join(sequence[idx:idx+n])
        if gram not in grams:
            grams.append(gram)
    return grams
#end def



if __name__ == '__main__':
    answer = n_gram(n        = 2, 
                    sequence = 'I am an NLPer'.split())
    print(answer)
    answer = n_gram(n        = 2, 
                    sequence = 'I am an NLPer'.replace(' ', ''))
    print(answer)
