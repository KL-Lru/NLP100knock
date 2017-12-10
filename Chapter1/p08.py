#
# 与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．
#   英小文字ならば(219 - 文字コード)の文字に置換
#   その他の文字はそのまま出力
#
def cipher(s):
  ret=""
  for i in range(len(s)):
    if s[i].islower() :
      ret+=chr(219-ord(s[i]))
    else:
      ret+=s[i]
  return ret
#end def

if __name__=="__main__":
  s="I love Yomi Natsusaki"
  print(s)
  and=cipher(s)
  print(ans)