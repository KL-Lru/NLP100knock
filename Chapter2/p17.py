#
# cut -f1 hightemp.txt | sort | uniq | wc -l
#

if __name__ == "__main__":
  file = open("hightemp.txt", "r")
  dic = {}
  for line in file.readlines():
    pref = line.split("\t")
    dic[pref[0]] = 0
  answer = len(dic)
  file.close()
  print(answer)