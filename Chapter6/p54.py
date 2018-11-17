from bs4 import BeautifulSoup as bs

if __name__ == '__main__':
  f = open('nlp.txt.xml')
  parse = bs(f.read(),'lxml')
  for i,j,k in zip(parse.find_all('word'),parse.find_all('lemma'),parse.find_all('pos')):
    print(i.get_text()+'\t'+j.get_text()+'\t'+k.get_text())