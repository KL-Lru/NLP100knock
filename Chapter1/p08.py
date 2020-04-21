# 与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．
#   英小文字ならば(219 - 文字コード)の文字に置換
#   その他の文字はそのまま出力

def cipher(text):
    return ''.join([
        chr(219 - ord(char)) if char.islower() else char 
        for char in text
    ])
#end def

if __name__ == '__main__':
    text = 'I love Yomi Natsusaki. She is so cute!'
    print(text)
    answer = cipher(text)
    print(answer)
