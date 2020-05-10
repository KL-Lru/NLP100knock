# ファイルを行単位でN分割せよ
# split -n l/N popular-names.txt

from p12 import fileOut

if __name__ == "__main__":
    n = int(input())
    fobj = open("popular-names.txt", "r")
    lines = fobj.readlines()
    lines_num = len(lines)
    sp_lines_num = lines_num // n
    ad_lines_num = lines_num % n
    line_cnt = 0
    print('Out split[0-9]+ .')
    for idx in range(n):
        qty = sp_lines_num + (1 if idx < ad_lines_num else 0)
        fileOut('split_' + str(idx), "".join(lines[line_cnt:line_cnt + qty]))
        line_cnt += qty
