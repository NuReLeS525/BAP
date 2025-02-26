from collections import defaultdict


#хочу решить эту задачу через классы
class Graph:
  def __init__(self, number_of_verticies):
    self.n = number_of_verticies
    self.graph = {node: [] for node in range(1, number_of_verticies+1)}
    for _ in self.graph:
      self.u, self.v = input().split()
      self.addEdge(int(self.u), int(self.v))

  def addEdge(self, u, v):
    self.u = u
    self.v = v
    self.graph[u].append(v)

  def printGraph(self):
    return print(self.graph)
  
graph = Graph(int(input()))
graph.printGraph()
