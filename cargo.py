import heapq
from collections import defaultdict

def max_capacity_path(graph, cities, start, end):

    pq = [(-float('inf'), start)]
    max_weight = {city: 0 for city in cities}
    max_weight[start] = float('inf')

    while pq:
        curr_weight, u = heapq.heappop(pq)
        curr_weight = -curr_weight

        if u == end:
            return curr_weight

        for v, weight in graph[u]:
            new_weight = min(curr_weight, weight)

            if new_weight > max_weight[v]:
                max_weight[v] = new_weight
                heapq.heappush(pq, (-new_weight, v))

    return -1

n, m = map(int, input().split())

graph = defaultdict(list)
cities = set()

for _ in range(m):
    a, b, w = input().split()
    w = int(w)
    graph[a].append((b, w))  # A → B
    cities.add(a)
    cities.add(b)

start, end = input().split()

result = max_capacity_path(graph, cities, start, end)
print(result)