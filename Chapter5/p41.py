# Chunkクラスを作れ

from p40 import Morph
import re

class Chunk:
    def __init__(self, dst):
        self.morphs = []
        self.dst = dst
        self.srcs = []

    def add_src(self, src):
        self.srcs.append(src)

    def add_morph(self, morph):
        self.morphs.append(morph)

    # 出力用関数
    def str_out(self):
        return f"{''.join([i.surface for i in self.morphs])} {self.dst} {self.srcs}"

    def morphs2str(self):
        return "".join([i.surface
                        for i in self.morphs
                        if i.surface != "。" and i.surface != "、"])
# end def Chunk

def getChunks():
    fobj = open("ai.ja.txt.parsed", "r")
    list_sentence = [] 
    sentence = []
    chunks = None
    for line in fobj.readlines():
        line = re.sub(r"( |\t)", ",", line.strip())
        elements = line.split(",")
        # next chunk
        if elements[0] == "*":
            if chunks is not None:
                sentence.append(chunks)
            dst = int(re.sub(r"^(-?[0-9]*)D", r"\1", elements[2]))
            chunks = Chunk(dst)
        # end sentence
        elif elements[0] == "EOS":
            if chunks is not None:
                sentence.append(chunks)
                chunks = None
            if sentence == []:
                continue
            for j in range(len(sentence)):
                if sentence[j].dst != -1:
                    sentence[sentence[j].dst].add_src(j)
            list_sentence.append(sentence)
            sentence = []
        # add morph
        else:
            chunks.add_morph(Morph(surf=elements[0],
                                   base=elements[7],
                                   pos=elements[1],
                                   pos1=elements[2]))
    fobj.close()
    return list_sentence
# end def getChunks


if __name__ == "__main__":
    list_sentence = getChunks()
    answer = "\n".join([i.str_out() for i in list_sentence[2]])
    print(answer)
