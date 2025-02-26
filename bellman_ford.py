import heapq
from collections import defaultdict


def Bellman_Ford(graph, src):
  dist = {node: float('inf') for node in graph}
  dist[src] = 0

  for _ in range(len(graph) - 1):
    for u in graph:
      for v, weight in graph[u]: # (1, 3) / (2, 5)
        if dist[u] != float('inf') and dist[u] + weight < dist[v]:
          dist[v] = dist[u] + weight

  for u in graph:
    for v, weight in graph[u]:
      if dist[u] != float('inf') and dist[u] + weight < dist[v]:
        # raise ValueError("Graph contains negative weight cycle")
        print('negative')
          
  return dist

graph = {
    0: [(1, 6), (2, 4)],
    1: [(2, 2)],
    2: [(3, -5)],
    3: [(0, -2), (1, 3)]
}

source = 0

distances = Bellman_Ford(graph, source)
print(distances)