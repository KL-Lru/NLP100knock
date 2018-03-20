#!/usr/bin/env python3
#
# tail -n N hightemp.txt
#

if __name__ == "__main__":
  n = int(input())
  cnt = 0
  file = open("hightemp.txt", "r")
  answer = ""
  for line in file.readlines()[::-1]:
    answer = line+answer
    cnt += 1
    if cnt == n:
      break
  file.close()
  print(answer)