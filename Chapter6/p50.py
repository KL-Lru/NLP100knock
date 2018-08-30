import re
from pprint import pprint

def getSentences():
  f = open("nlp.txt")
  txt = re.sub("([\.\;\:\?\!]) ([A-Z])", "\\1\n\\2",f.read().replace("\n"," "))
  return txt.split("\n")

print("\n".join(getSentences()))