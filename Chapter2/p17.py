# 1列目の文字列の種類数を求めよ
# cut -f1 popular-names.txt | sort | uniq | wc -l

if __name__ == "__main__":
    fobj = open("popular-names.txt", "r")
    prefs = set()
    for line in fobj.readlines():
        pref = line.split("\t")
        prefs.add(pref[0])
    fobj.close()
    answer = len(prefs)
    print(answer)
