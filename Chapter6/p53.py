from bs4 import BeautifulSoup as bs

if __name__ == '__main__':
  f = open('nlp.txt.xml')
  parse = bs(f.read(),'lxml')
  for i in parse.find_all("word"):
    print(i.get_text())
