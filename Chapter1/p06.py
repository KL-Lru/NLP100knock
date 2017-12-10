#
# 文字bi-gramの集合を，それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．
# さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．
#
import p05 
import pprint as p

s1="paraparaparadise"
s2="paragraph"
x=set(p05.n_gram(n=2,mode='c',s=s1))
y=set(p05.n_gram(n=2,mode='c',s=s2))
ans=[]
ans.append(["uni",x.union(y)])
ans.append(["pro",x.intersection(y)])
ans.append(["dif",x.symmetric_difference(y)])
ans.append(["se in x?","se" in x])
ans.append(["se in y?","se" in y])
p.pprint(ans)
