#
# 係り受け関係を図示せよ
#

import pydot
from p41 import getChunk

if __name__ == "__main__":
  list_sent = getChunk()
  a=1
  for sent in list_sent:
    edge=[]
    for chunkn in range(len(sent)):
      if sent[chunkn].dst != -1:
        src=sent[chunkn].morst()
        dst=sent[sent[chunkn].dst].morst()
        edge.append(((chunkn,src),(sent[chunkn].dst,dst)))
    graph=pydot.Dot(graph_type='digraph')
    for i in edge:
      graph.add_node(pydot.Node(i[0][0],label=i[0][1]))
      graph.add_node(pydot.Node(i[1][0],label=i[1][1]))
      graph.add_edge(pydot.Edge(i[0][0],i[1][0]))
    graph.write_png('graph'+str(a)+'.png')
    a+=1
    print(a)