#
# 文を単語に分解し，各単語の文字数を先頭から出現順に並べたリストを作成せよ．
#
s="Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
ans=[]
for i in s.replace(","," ").replace("."," ").split():
  ans.append(len(i))
print(ans)