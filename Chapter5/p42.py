#
# 係り受け関係を示せ
#

from re import sub
from pprint import pprint
from p41 import getChunk

if __name__ == "__main__":
    l=getChunk()
    for i in l:
        for j in i:
            if j.dst != -1:
                print(j.morst()+'\t'+i[j.dst].morst())
