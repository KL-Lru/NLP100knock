#
# 与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．
# この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．
#
def n_gram(n,mode,s):
  ret=[]
  ret_unic=[]
  if mode=='w':
    l=s.split()
    tp=[]
    for i in range(len(l)-n+1):
      ret.append(" ".join(l[i:i+n:1]))
  elif mode=='c':
    s1=s.replace(" ","")
    for i in range(len(s1)-n+1):
      ret.append(s1[i:i+n:1])
  for i in ret:
    if i not in ret_unic:
      ret_unic.append(i)
  return ret_unic
#end def

if __name__=="__main__":
  ans=n_gram(n=2,mode='w',s="I am an NLPer")
  print(ans)
  ans=n_gram(n=2,mode='c',s="I am an NLPer")
  print(ans)