from p51 import getWords
from nltk.stem.porter import PorterStemmer

if __name__ == '__main__':
  ps = PorterStemmer()
  for si in getWords():
    for wi in si:
      wstem = ps.stem(wi)
      print(wstem + '\t' + wi[len(wstem):])