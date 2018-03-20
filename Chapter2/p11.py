#!/usr/bin/env python3
#
# sed "s/\t/ /g" hightemp.txt
#

if __name__ == "__main__":
  file=open("hightemp.txt", "r")
  answer=file.read().replace("\t", " ")
  file.close()
  print(answer)