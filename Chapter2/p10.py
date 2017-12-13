#
# wc -l hightemp.txt
#
f=open("hightemp.txt","r")
ans=len(f.readlines())
f.close()
print(ans)