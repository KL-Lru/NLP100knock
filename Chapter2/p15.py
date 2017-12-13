#
# tail -n N hightemp.txt
#
n=int(input())
cnt=0
f=open("hightemp.txt","r")
ans=""
for i in f.readlines()[::-1]:
  ans=i+ans
  cnt+=1
  if cnt == n:
    break
print(ans)