# スペースで区切られた単語列のうち長さが4より大きい単語に対して，各単語の先頭と末尾の文字は残し，それ以外の文字の順序をランダムに並び替えよ

import random

if __name__ == "__main__":
    text = """
        I couldn't believe that I could actually understand what I was reading 
        : the phenomenal power of the human mind .
        """
    words = text.split()
    for idx in range(len(words)):
        if len(words[idx]) > 4 :
            words[idx] = words[idx][0] \
                      + "".join(random.sample(words[idx][1:-1], len(words[idx])-2)) \
                      + words[idx][-1]
    answer = " ".join(words)
    print(answer)