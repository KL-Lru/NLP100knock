# 3列目を基準に各行を逆順ソートせよ
# sort -k3r popular-names.txt

if __name__ == "__main__":
    fobj = open("popular-names.txt", "r")
    lines = fobj.readlines()
    lines.sort(key = lambda x: x.split()[2], reverse=True)
    answer = "".join(lines)
    fobj.close()
    print(answer)
