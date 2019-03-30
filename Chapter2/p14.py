# 先頭N行を出力せよ
# head -n N hightemp.txt

if __name__ == "__main__":
    n      = int(input())
    cnt    = 0
    answer = ""
    fobj = open("hightemp.txt", "r")
    for line in fobj.readlines():
        answer += line
        cnt    += 1
        if cnt == n:
            break
    fobj.close()
    print(answer)
