#
# split -l N hightemp.txt
#
from math import ceil
n=int(input())
f=open("hightemp.txt","r")
s=f.readlines()
f.close()
ip=ceil(len(s)/n)
for i in range(n):
  f=open("split_txt"+str(i),"w+")
  f.write("".join(s[ip*i:ip*(i+1)] if i!=n-1 else s[ip*i:]))
  f.close()