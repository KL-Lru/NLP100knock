from bs4 import BeautifulSoup as bs
#java -Xmx2g -cp "/usr/local/lib/stanford-corenlp-full-2018-02-27/*" edu.stanford.nlp.pipeline.StanfordCoreNLP -annotators "tokenize,ssplit,pos,lemma,ner,regexner,truecase,parse,depparse,dcoref,relation,natlog,quote,sentiment" -file nlp.txt -outputFormat xml

if __name__ == '__main__':
  f = open('nlp.txt.xml')
  parse = bs(f.read(),'lxml')
  for i in parse.find_all("word"):
    print(i.get_text())
