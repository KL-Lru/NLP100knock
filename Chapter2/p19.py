# 1列目の出現頻度順に出力せよ
# cut -f1 popular-names.txt | sort | uniq -c | sort -r | awk '{print $2}'

if __name__ == "__main__":
    fobj = open("popular-names.txt", "r")
    prefs = [line.split("\t")[0] for line in fobj.readlines()]
    prefset = list(set(prefs))
    prefset.sort(key = lambda x:prefs.count(x), reverse=True)
    answer = "\n".join(prefset)
    fobj.close()
    print(answer)
