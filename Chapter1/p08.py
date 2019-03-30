# 与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．
#   英小文字ならば(219 - 文字コード)の文字に置換
#   その他の文字はそのまま出力

def cipher(text):
    converted = ""
    for char in text:
        if char.islower() :
            converted += chr(219-ord(char))
        else:
          converted += char
    return converted
#end def

if __name__ == "__main__":
    text = "I love Yomi Natsusaki"
    print(text)
    answer = cipher(text)
    print(answer)