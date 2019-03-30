# 2つのファイルを連結せよ
# paste col1.txt col2.txt

if __name__ == "__main__":
    fobj1 = open("col1.txt", "r")
    fobj2 = open("col2.txt", "r")
    answer = ""
    for (fi, fj) in zip(fobj1.readlines(), fobj2.readlines()):
        answer += fi[:-1] + "\t" + fj
    fobj1.close()
    fobj2.close()
    print(answer)
