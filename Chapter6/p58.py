from bs4 import BeautifulSoup as bs

if __name__ == '__main__':
  f = open('nlp.txt.xml')
  parse = bs(f.read(), 'lxml')
  sentences = parse.find('sentences')
  for sentence in sentences.find_all('sentence'):
    d = {}
    for i, token in enumerate([x.find('word').get_text() for x in sentence.find_all('token')]):
      d[i+1] = {}
      d[i+1]['word'] = token
    coll_dep = sentence.find('dependencies', {'type':'collapsed-dependencies'})
    for dep in coll_dep.find_all('dep', {'type':'nsubj'}):
      gov = dep.find('governor')
      de = dep.find('dependent')
      d[int(gov.get('idx'))]['nsubj'] = de.get_text()
    for dep in coll_dep.find_all('dep', {'type':'dobj'}):
      gov = dep.find('governor')
      de = dep.find('dependent')
      d[int(gov.get('idx'))]['dobj'] = de.get_text()
    for key in d:
      if 'word' in d[key] and 'nsubj' in d[key] and 'dobj' in d[key]:
        print(d[key]['nsubj']+'\t'+d[key]['word']+'\t'+d[key]['dobj'])
