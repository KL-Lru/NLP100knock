#!/usr/bin/env python3
#
# cut -f 1 hightemp.txt > col1.txt
# cut -f 2 hightemp.txt > col2.txt
#

if __name__ == "__main__":
  file = open("hightemp.txt", "r")
  col1 = []
  col2 = []
  for line in file.readlines():
    col=line[:-1].split("\t") #改行文字は切り捨てる
    col1.append(col[0])
    col2.append(col[1])
  file.close()
  file=open("col1.txt", "w+")
  file.write("\n".join(col1) + "\n")
  file.close()
  file=open("col2.txt", "w+")
  file.write("\n".join(col2) + "\n")
  file.close()
