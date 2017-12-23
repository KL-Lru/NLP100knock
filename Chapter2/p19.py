#
# cut -f1 hightemp.txt | sort | uniq -c | sort -r | awk '{print $2}'
#
# 内包表現とlambda式が少しわかって来たので書いてみた感
f=open("hightemp.txt","r")
read=[x.split("\t")[0] for x in f.readlines()]
s=set()
#s.add(x)の返り値はNone(False),評価はしたいのでand,前半のboolを変えぬようnot
li=[[read.count(x),x] for x in read if x not in s and not s.add(x)]
li.sort(key=lambda x: x[0])
li.reverse()
ans="\n".join([x[1] for x in li])
print(ans)