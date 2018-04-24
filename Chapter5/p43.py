#
# 名詞を含む文節⇒動詞を含む文節を抽出
#
from p41 import Chunk
from p41 import getChunk

def contain_noun(chunk):
    for morph in chunk.morphs:
        if morph.pos == "名詞":
            return True
    return False

def contain_verb(chunk):
    for morph in chunk.morphs:
        if morph.pos == "動詞":
            return True
    return False

if __name__ =="__main__":
    list_sent=getChunk()
    for sent in list_sent:
        for chunk in sent:
            if contain_noun(chunk) and contain_verb(sent[chunk.dst]):
                print(chunk.morst() + '\t' + sent[chunk.dst].morst())