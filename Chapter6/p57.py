#!/usr/bin/env/python3
#
# 係り受け関係を図示せよ
#

import pydot
from bs4 import BeautifulSoup as bs
from pprint import pprint

if __name__ == '__main__':
  f = open('nlp.txt.xml')
  parse = bs(f.read(),'lxml')
  sentences = parse.find('sentences')
  graph_num = 0
  for sentence in sentences.find_all('sentence'):
    graph = pydot.Dot(graph_type = 'digraph')
    coll_dep = sentence.find('dependencies', {'type':'collapsed-dependencies'})
    for dep in coll_dep.find_all('dep'):
      src = dep.find('governor')
      dst = dep.find('dependent')
      if src.get('idx') == '0' or src.get_text() == ',' or src.get_text() == '.' or dst.get_text() == ',' or dst.get_text() == '.':
        continue
      graph.add_node(pydot.Node(int(src.get('idx')), label = src.get_text()))
      graph.add_node(pydot.Node(int(dst.get('idx')), label = dst.get_text()))
      graph.add_edge(pydot.Edge(int(src.get('idx')), int(dst.get('idx'))))
    graph.write_png('graph' + str(graph_num) + '.png')
    graph_num += 1
