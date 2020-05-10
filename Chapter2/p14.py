# 先頭N行を出力せよ
# head -n N popular-names.txt

if __name__ == "__main__":
    n      = int(input())
    fobj   = open("popular-names.txt", "r")
    answer = "".join(fobj.readlines()[:n])
    fobj.close()
    print(answer)
