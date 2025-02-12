import heapq

def Dijkstra(graph, start):
  n = len(graph)
  dist = {node: float('inf') for node in graph}
  dist[start] = 0
  pq = [(0, start)]

  while pq:
    current_dist, u = heapq.heappop(pq)

    if current_dist > dist[u]:
      continue

    for v, weight in graph[u]:
      new_dist = current_dist + weight
      if new_dist < dist[v]:
        dist[v] = new_dist
        heapq.heappush(pq, (new_dist, v))

  return dist


graph = {
  1: [(2, 2), (3, 1), (4, 1)],
  2: [(5, 3)],
  3: [(5, 2), (6, 1), (7, 2)],
  4: [(7, 1)],
  5: [(8, 2)],
  6: [(8, 2), (9, 2)],
  7: [(9, 1)],
  8: [],
  9: []
}

starting = 1

paths = Dijkstra(graph, starting)
print(paths)