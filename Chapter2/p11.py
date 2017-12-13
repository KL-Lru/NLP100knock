#
# sed "s/\t/ /g" hightemp.txt
#
f=open("hightemp.txt","r")
ans=f.read().replace("\t"," ")
f.close()
print(ans)