#
# cut -f1 hightemp.txt | sort | uniq | wc -l
#
f=open("hightemp.txt","r")
li={}
for i in f.readlines():
  ti=i.split("\t")
  li[ti[0]]=ti[1:-1]
ans=[]
for i in li:
  ans.append(i)
print(len(ans))