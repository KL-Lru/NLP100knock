#!/usr/bin/env python3
#
# sort -k3 hightemp.txt
#

if __name__ == "__main__":
  file = open("hightemp.txt", "r")
  lines = [line.split() for line in file.readlines()]
  # lambda式使うとこれだけで出来る
  # lines.sort(key=lambda x:x[2]) 
  # 以下無難なバブルソート
  for i in range(len(lines)):
    for j in range(len(lines)-1, i, -1):
      if lines[j][2] < lines[j-1][2]:
        tmp = lines[j]
        lines[j] = lines[j-1]
        lines[j-1] = tmp
  for i in range(len(lines)):
    lines[i] = "\t".join(lines[i])
  answer = "".join(lines)
  file.close()
  print(answer)