#
# サ変接続の名詞を全て抽出せよ
#

from p30 import get_mecab

analy=get_mecab()
ans=[]
for i in analy:
  for j in i:
    if j["pos1"]=="サ変接続":
      ans.append(j["base"])
print(ans)