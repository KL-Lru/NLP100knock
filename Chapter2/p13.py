#
# paste col1.txt col2.txt
#

if __name__ == "__main__":
  file1 = open("col1.txt", "r")
  file2 = open("col2.txt", "r")
  answer = ""
  for (fi, fj) in zip(file1.readlines(), file2.readlines()):
    answer += fi[:-1] + "\t" + fj
  file1.close()
  file2.close()
  print(answer)