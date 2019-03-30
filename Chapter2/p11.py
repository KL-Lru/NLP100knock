# タブをスペースに置換せよ
# sed "s/\t/ /g" hightemp.txt

if __name__ == "__main__":
    fobj = open("hightemp.txt", "r")
    answer = fobj.read().replace("\t", " ")
    fobj.close()
    print(answer)
