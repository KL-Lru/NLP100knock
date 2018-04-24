#
# 名詞を含む文節⇒動詞を含む文節を抽出
#
from p41 import Chunk
from p41 import getChunk

def contain_noun(c):
    for i in c.morphs:
        if i.pos == "名詞":
            return True
    return False

def contain_verb(c):
    for i in c.morphs:
        if i.pos == "動詞":
            return True
    return False

if __name__ =="__main__":
    l=getChunk()
    for i in l:
        for j in i:
            if contain_noun(j) and contain_verb(i[j.dst]):
                print(j.morst()+'\t'+i[j.dst].morst())