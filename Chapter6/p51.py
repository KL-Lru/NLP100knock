from p50 import getSentences

def getWords():
  sents = getSentences()
  words = [x.split() for x in sents]
  return words

print("\n\n".join(["\n".join(x) for x in getWords()]))