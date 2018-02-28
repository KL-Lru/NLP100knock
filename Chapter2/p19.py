#
# cut -f1 hightemp.txt | sort | uniq -c | sort -r | awk '{print $2}'
#

if __name__ == "__main__":
  file = open("hightemp.txt", "r")
  pref = [x.split("\t")[0] for x in file.readlines()]
  s = set()
  cnt_pref = []
  # 内包表現でもいけるけど読みづらい
  # cnt_pref = [[pref.count(x), x] for x in pref if x not in s and not s.add(x)]
x  for pi in pref:
    if pi not in s:
      s.add(pi)
      cnt_pref.append([pref.count(pi), pi])
  # lambda式使うとこれだけで出来る
  # cnt_pref.sort(key=lambda x:x[0]) 
  # 以下無難なバブルソート
  for i in range(len(cnt_pref)):
    for j in range(len(cnt_pref)-1, i, -1):
      if cnt_pref[j][0] < cnt_pref[j-1][0]:
        tmp = cnt_pref[j]
        cnt_pref[j] = cnt_pref[j-1]
        cnt_pref[j-1] = tmp
  cnt_pref.reverse()
  answer = "\n".join([x[1] for x in cnt_pref])
  file.close()
  print(answer)