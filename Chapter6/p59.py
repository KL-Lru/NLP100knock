from bs4 import BeautifulSoup as bs
import re

def getNest(li):
  depth = 0
  for i, ele in enumerate(li):
    if ele == '(':
      depth += 1
    elif ele == ')':
      depth -= 1
    if depth == 0:
      return li[:i+1]

def parseNest(li):
  s = ''
  lo = False
  for i, ele in enumerate(li):
    if ele == ')':
      continue
    elif ele == '(':
      lo = True
    else:
      if lo:
        lo = False
        continue
      s += ('' if s == '' else ' ') + ele
  return s

if __name__ == '__main__':
  f = open('nlp.txt.xml')
  parse = bs(f.read(), 'lxml')
  sentences = parse.find('sentences')
  for sentence in sentences.find_all('sentence'):
    s = sentence.find('parse').get_text()
    s = re.sub('\(', '( ', s)
    s = re.sub('\)', ' )', s)
    st = s.split()
    for i, ele in enumerate(st):
      if ele == 'NP':
        nested = getNest(st[i-1:])
        print(parseNest(nested))