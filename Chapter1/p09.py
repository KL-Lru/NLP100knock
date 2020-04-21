# スペースで区切られた単語列のうち長さが4より大きい単語に対して，各単語の先頭と末尾の文字は残し，それ以外の文字の順序をランダムに並び替えよ

import random

def shuffle(segment):
    return ''.join(random.sample(segment, len(segment)))

if __name__ == '__main__':
    text = '''
        I couldn't believe that I could actually understand what I was reading 
        : the phenomenal power of the human mind .
    '''
    words = text.split()
    shuffled_words = [
        word if len(word) <= 4 else word[0] + shuffle(word[1:-1]) + word[-1]
        for word in words
    ]
    answer = ' '.join(shuffled_words)
    print(answer)