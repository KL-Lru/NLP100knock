#
# paste col1.txt col2.txt
#
f1=open("col1.txt","r")
f2=open("col2.txt","r")
ans=""
for (i,j) in zip(f1.readlines(),f2.readlines()):
  ans+=i[:-1]+"\t"+j
f1.close()
f2.close()
print(ans)