# 形態素解析結果を読み込め

# mecab -F "%m,%H\n" neko.txt > neko.txt.mecab
# ↑これでmecabファイルを作ると区切りが全てカンマになるので楽になる

from pprint import pprint


def getMecabData():
    fobj = open("neko.txt.mecab", "r")
    res = []
    sentence = []
    for line in fobj.readlines():
        line = line.strip()
        if line == "": 
            continue
        if line == "EOS":
            res.append(sentence)
            sentence = []
            continue
        else:
            word = line.split(",")
            if word[0] == "":
                continue
            info = {"surface": word[0],
                    "base"   : word[7],
                    "pos"    : word[1],
                    "pos1"   : word[2]}
            sentence.append(info)
    return res
# end def

if __name__ == "__main__":
    answer = getMecabData()
    pprint(answer)
