#
#文を単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，それ以外の単語は先頭に2文字を取り出し，取り出した文字列から単語の位置への連想配列を作成せよ．
#
s="Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
words=s.replace(","," ").replace("."," ").split()
tar=[1,5,6,7,8,9,15,16,19]
ans={}
for i in range(0,len(words),1):
  ans[words[i][0:1 if i in tar else 2:1]]=i
print(ans)
