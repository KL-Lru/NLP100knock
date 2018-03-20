#!/usr/bin/env python3
#
# head -n N hightemp.txt
#

if __name__ == "__main__":
  n = int(input())
  cnt = 0
  file = open("hightemp.txt", "r")
  answer = ""
  for line in file.readlines():
    answer += line
    cnt += 1
    if cnt == n:
      break
  file.close()
  print(answer)