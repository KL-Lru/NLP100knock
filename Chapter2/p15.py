# 末尾N行を出力せよ
# tail -n N hightemp.txt

if __name__ == "__main__":
    n      = int(input())
    cnt    = 0
    answer = ""
    fobj = open("hightemp.txt", "r")
    for line in fobj.readlines()[::-1]:
        answer = line + answer
        cnt    += 1
        if cnt == n:
            break
    fobj.close()
    print(answer)
