#
# split -l N hightemp.txt
#

from math import ceil

if __name__ == "__main__":
  n = int(input())
  file = open("hightemp.txt", "r")
  lines = file.readlines()
  line_num= len(lines)
  file.close()
  lf_point = 0
  for i in range(n):
    br_point = ceil((line_num-lf_point) / (n-i))
    file = open("split_txt" + str(i), "w+")
    file.write("".join(lines[lf_point : lf_point+br_point]))
    lf_point += br_point
    file.close()