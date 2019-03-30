# 3列目を基準に各行を逆順ソートせよ
# sort -k3r hightemp.txt

if __name__ == "__main__":
    fobj = open("hightemp.txt", "r")
    lines = [line.split() for line in fobj.readlines()]
    lines.sort(key = lambda x:x[2])
    lines.reverse()
    # 分割したので復元する
    for idx in range(len(lines)):
        lines[idx] = "\t".join(lines[idx])
    answer = "\n".join(lines)
    fobj.close()
    print(answer)
