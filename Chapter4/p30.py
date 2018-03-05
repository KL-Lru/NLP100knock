# mecab -F "%m,%H\n" neko.txt > neko.txt.mecab
# 
# 形態素解析結果を読み込め
#

from pprint import pprint

def get_mecab():
  f=open("neko.txt.mecab","r")
  res=[]
  sent=[]
  for line in f.readlines():
    if line == "EOS\n":
      res.append(sent)
      sent=[]
      continue
    analy=line[:-1].split(",") #改行記号抜き
    s={"surface":analy[0],
      "base":analy[7],
      "pos":analy[1],
      "pos1":analy[2]}
    sent.append(s)
  return res

if __name__ == "__main__":
  pprint(get_mecab())