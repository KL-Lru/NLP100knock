#
# 名詞の連接を最長一致で全て抽出せよ
#

from p30 import get_mecab

analy=get_mecab()
ans=[]
for i in analy:
  noun=""
  cnt=0
  for j in range(len(i)):
    if i[j]["pos"]=="名詞":
      noun=noun+i[j]["surface"]
      cnt+=1
    elif cnt>=2:
      ans.append(noun)
      cnt=0
      noun=""
    else:
      cnt=0
      noun=""
print(ans)