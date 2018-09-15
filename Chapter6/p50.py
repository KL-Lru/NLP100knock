import re
from pprint import pprint

def getSentences():
  f = open("nlp.txt")
  txt = re.sub("([\.\;\:\?\!]) ([A-Z])", "\\1\n\\2",f.read())
  txt = re.sub("\\n\\n","\n",txt)
  return txt.split("\n")

if __name__ == '__main__':
  print("\n".join(getSentences()))