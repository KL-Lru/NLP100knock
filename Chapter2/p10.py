# 行数をカウントせよ
# wc -l popular-names.txt

if __name__ == "__main__":
    fobj = open("popular-names.txt", "r")
    answer = len(fobj.readlines())
    fobj.close()
    print(answer)
