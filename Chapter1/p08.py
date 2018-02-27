#
# 与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．
#   英小文字ならば(219 - 文字コード)の文字に置換
#   その他の文字はそのまま出力
#
def cipher(text):
  res = ""
  for i in range(len(text)):
    if text[i].islower() :
      res+=chr(219-ord(text[i]))
    else:
      res+=text[i]
  return res
#end def

if __name__ == "__main__":
  text = "I love Yomi Natsusaki"
  print(text)
  answer = cipher(text)
  print(answer)