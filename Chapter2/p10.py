# 行数をカウントせよ
# wc -l hightemp.txt

if __name__ == "__main__":
    fobj = open("hightemp.txt", "r")
    answer = len(fobj.readlines())
    fobj.close()
    print(answer)
