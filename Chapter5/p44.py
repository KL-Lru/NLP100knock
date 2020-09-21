# 係り受け関係を図示せよ

import pydot
from p41 import getChunks

if __name__ == "__main__":
  graph_num = 0
  for sentence in getChunks()[:4]:
    edges = []
    for cn in range(len(sentence)):
      if sentence[cn].dst != -1:
        src = sentence[cn].morphs2str()
        dst = sentence[sentence[cn].dst].morphs2str()
        edges.append(((cn, src),
                      (sentence[cn].dst, dst)
                    ))
    graph = pydot.Dot(graph_type = 'digraph')
    for edge in edges:
      graph.add_node(pydot.Node(edge[0][0], label = edge[0][1]))
      graph.add_node(pydot.Node(edge[1][0], label = edge[1][1]))
      graph.add_edge(pydot.Edge(edge[0][0], edge[1][0]))
    graph.write_png('graph' + str(graph_num) + '.png')
    graph_num += 1
