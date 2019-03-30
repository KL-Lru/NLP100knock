# 1列目と2列目をそれぞれ他のファイルに出力せよ
# cut -f 1 hightemp.txt > col1.txt
# cut -f 2 hightemp.txt > col2.txt

def fileOut(filename, text):
    fobj = open(filename, 'w+')
    fobj.write(text)
    fobj.close()
# end def

if __name__ == "__main__":
    fobj = open("hightemp.txt", "r")
    col1 = []
    col2 = []
    for line in fobj.readlines():
        cols = line[:-1].split("\t")  # 改行文字は切り捨てる
        col1.append(cols[0])
        col2.append(cols[1])
    fobj.close()
    print('Out col1.txt, col2.txt .')
    fileOut('col1.txt', "\n".join(col1) + "\n")
    fileOut('col2.txt', "\n".join(col1) + "\n")
