# Morphクラスを作れ

import re

class Morph:
    def __init__(self, surf, base, pos, pos1):
        self.surface = surf
        self.base = base
        self.pos = pos
        self.pos1 = pos1
    # end init

    def __repr__(self):
        return f"{self.surface}\t{self.base}\t{self.pos}\t{self.pos1}"
    # end repr
# end Morph

def getMorphs():
    fobj = open("ai.ja.txt.parsed", "r")
    list_sentence = []
    sentence = []
    for line in fobj.readlines():
        line = re.sub(r"( |\t)", ",", line.strip())
        elements = line.split(",")
        if elements[0] == "*":
            continue
        elif elements[0] == "EOS":
            if sentence == []:
                continue
            list_sentence.append(sentence)
            sentence = []
        else:
            sentence.append(Morph(surf=elements[0],
                                  base=elements[7],
                                  pos=elements[1],
                                  pos1=elements[2]))
    fobj.close()
    return list_sentence
# end def getMorphs


if __name__ == "__main__":
    list_sentence = getMorphs()
    answer = "".join([i.surface for i in list_sentence[1]])
    print(answer)
