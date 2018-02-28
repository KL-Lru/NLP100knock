#
# wc -l hightemp.txt
#

if __name__ == "__main__":
  file = open("hightemp.txt", "r")
  answer = len(file.readlines())
  file.close()
  print(answer)