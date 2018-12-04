from bs4 import BeautifulSoup as bs
from pprint import pprint

if __name__ == '__main__':
  f = open('nlp.txt.xml')
  parse = bs(f.read(),'lxml')
  sentences = parse.find('sentences')
  ss = []
  for sentence in sentences.find_all('sentence'):
    tk = []
    for token in sentence.find_all('token'):
      tk.append(token.find('word').get_text())
    ss.append(tk)
  for cor in parse.find_all('coreference')[1:]:
    repcor = cor.find('mention',{"representative":"true"}).find('text').get_text()
    for mention in cor.find_all('mention'):
      if mention.find('text').get_text() == repcor:
        continue
      sent = int(mention.find('sentence').get_text())
      start = int(mention.find('start').get_text())
      end = int(mention.find('end').get_text())
      ss[sent-1][start-1] = repcor + '(' + ss[sent-1][start-1]
      ss[sent-1][end-2] = ss[sent-1][end-2] + ')'
  print('\n'.join([' '.join(sentence) for sentence in ss]))
