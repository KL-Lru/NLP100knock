#
# 動詞の表層系を全て抽出せよ
#

from p30 import get_mecab

analy=get_mecab()
ans=[]
for i in analy:
  for j in i:
    if j["pos"]=="動詞":
      ans.append(j["surface"])
print(ans)