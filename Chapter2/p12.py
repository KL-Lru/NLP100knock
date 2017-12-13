#
# cut -f 1 hightemp.txt > col1.txt
# cut -f 2 hightemp.txt > col2.txt
#
f=open("hightemp.txt","r")
col1=[]
col2=[]
for i in f.readlines():
  col=i[:-1].split("\t")
  col1.append(col[0])
  col2.append(col[1])
f.close()
f=open("col1.txt","w+")
f.write("\n".join(col1)+"\n")
f.close()
f=open("col2.txt","w+")
f.write("\n".join(col2)+"\n")
f.close()
