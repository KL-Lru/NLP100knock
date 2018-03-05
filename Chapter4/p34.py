#
# 「AのB」となる名詞句を全て抽出せよ
#

from p30 import get_mecab

analy=get_mecab()
ans=[]

for i in analy:
  for j in range(len(i)-2):
    if i[j]["pos"]=="名詞" and i[j+1]["surface"]=="の" and i[j+2]["pos"]=="名詞":
      ans.append(i[j]["surface"]\
                +i[j+1]["surface"]\
                +i[j+2]["surface"])
print(ans)