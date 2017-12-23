#
# sort -k3 hightemp.txt
#
f=open("hightemp.txt","r")
ans=[]
for i in f.readlines():
  ans.append(i.split("\t"))
# lambda式使うとこれだけで出来る、無難なバブルソートも書いた
# ans.sort(key=lambda x:x[2]) 
for i in range(len(ans)):
  for j in range(len(ans)-1,i,-1):
    if ans[j][2] < ans[j-1][2]:
      tmp=ans[j]
      ans[j]=ans[j-1]
      ans[j-1]=tmp
for i in range(len(ans)):
  ans[i]="\t".join(ans[i])
ans="".join(ans)
print(ans)