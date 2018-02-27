#
# スペースで区切られた単語列のうち長さが4より大きい単語に対して，各単語の先頭と末尾の文字は残し，それ以外の文字の順序をランダムに並び替えろ
#
from random import sample

if __name__ == "__main__":
  text="""
    I couldn't believe that I could actually understand what I was reading 
    : the phenomenal power of the human mind .
    """
  words = text.split()
  for i in range(len(words)):
    if len(words[i]) > 4 :
      words[i] = words[i][0] \
                 + "".join(sample(words[i][1:-1], len(words[i])-2)) \
                 + words[i][-1]
  answer = " ".join(words)
  print(answer)