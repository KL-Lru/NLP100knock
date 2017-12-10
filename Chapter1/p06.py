#
# 文字bi-gramの集合を，それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．
# さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．
#
import p05 
import pprint as p

def uni(l1,l2):
  ret=l1+l2
  ret_unic=[]
  for i in ret:
    if i not in ret_unic:
      ret_unic.append(i)
  return ret_unic

def pro(l1,l2):
  ret=[]
  for i in l1:
    if i in l2:
      ret.append(i)
  return ret

def dif(l1,l2):
  ret=[]
  for i in l1:
    if i not in l2:
      ret.append(i)
  for i in l2:
    if i not in l1:
      ret.append(i)
  return ret

if __name__=='__main__':
  s1="paraparaparadise"
  s2="paragraph"
  x=p05.n_gram(n=2,mode='c',s=s1)
  y=p05.n_gram(n=2,mode='c',s=s2)
  ans=[]
  ans.append(["uni",uni(x,y)])
  ans.append(["pro",pro(x,y)])
  ans.append(["dif",dif(x,y)])
  ans.append(["se in x?","se" in x])
  ans.append(["se in y?","se" in y])
  p.pprint(ans)
