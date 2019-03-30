# 1列目の出現頻度順に県名を出力せよ
# cut -f1 hightemp.txt | sort | uniq -c | sort -r | awk '{print $2}'

if __name__ == "__main__":
    fobj = open("hightemp.txt", "r")
    prefs = [line.split("\t")[0] for line in fobj.readlines()]
    pref_set = set()
    cnt_pref = [[prefs.count(pref), pref]
                 for pref in prefs
                 if pref not in pref_set and not pref_set.add(pref)] 
    cnt_pref.sort(key = lambda pref_t:pref_t[0])
    cnt_pref.reverse()
    answer = "\n".join([pref_t[1] for pref_t in cnt_pref])
    fobj.close()
    print(answer)
