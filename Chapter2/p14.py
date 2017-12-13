#
# head -n N hightemp.txt
#
n=int(input())
cnt=0
f=open("hightemp.txt","r")
ans=""
for i in f.readlines():
  ans+=i
  cnt+=1
  if cnt == n:
    break
print(ans)