import re
from p50 import getSentences

def getWords():
  sents = getSentences()
  words = [re.sub("[\,\.\:\;\?\!]","",x).split() for x in sents]
  return words

if __name__ == '__main__':
  print("\n\n".join(["\n".join(x) for x in getWords()]))