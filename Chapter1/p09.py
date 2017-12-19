#
# スペースで区切られた単語列のうち長さが4より大きい単語に対して，各単語の先頭と末尾の文字は残し，それ以外の文字の順序をランダムに並び替えろ
#
import random
s="I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
l=s.split()
for i in range(len(l)):
  if len(l[i])>4 :
    l[i]=l[i][0]+"".join(random.sample(l[i][1:-1],len(l[i])-2))+l[i][-1]
ans=" ".join(l)
print(ans)