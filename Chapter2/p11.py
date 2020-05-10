# タブをスペースに置換せよ
# sed "s/\t/ /g" popular-names.txt

if __name__ == "__main__":
    fobj = open("popular-names.txt", "r")
    answer = fobj.read().replace("\t", " ")
    fobj.close()
    print(answer)
