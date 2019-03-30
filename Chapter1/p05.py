# 与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．
# この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．

def n_gram(n, mode, text):
    grams = []
    if mode == 'word':
        words = text.split()
        for idx in range(len(words) - n+1):
            gram = " ".join(words[idx:idx+n])
            if gram not in grams:
                grams.append(gram)
    elif mode == 'char':
        chars = text.replace(" ", "")
        for idx in range(len(chars) - n+1):
            gram = chars[idx:idx+n:1]
            if gram not in grams:
                grams.append(gram)
    return grams
#end def

if __name__ == "__main__":
    answer = n_gram(n    = 2, 
                    mode = 'word', 
                    text = "I am an NLPer")
    print(answer)
    answer = n_gram(n    = 2, 
                    mode = 'char', 
                    text = "I am an NLPer")
    print(answer)
