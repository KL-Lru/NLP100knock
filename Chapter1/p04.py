# 文を単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，
# それ以外の単語は先頭に2文字を取り出し，取り出した文字列から単語の位置への連想配列を作成せよ．

if __name__ == '__main__':
    text = '''
        Hi He Lied Because Boron Could Not Oxidize Fluorine. 
        New Nations Might Also Sign Peace Security Clause. 
        Arthur King Can.
    '''
    target = [
        1, 5, 6,
        7, 8, 9,
        15, 16, 19
    ]
    words  = [
        ti.strip(', .') for ti in text.split()
    ]
    answer = {
        words[idx][:(1 if idx+1 in target else 2)] : idx
        for idx in range(len(words))
    }
    print(answer)
