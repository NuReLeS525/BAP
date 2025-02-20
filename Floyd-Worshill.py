INF = float('inf') 

def floyd_warshall(graph):
    n = len(graph)
    
    dist = [row[:] for row in graph]
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    return dist

graph = [
    [0, 3, INF, INF, INF, 7],
    [3, 0, 1, INF, INF, INF],
    [INF, 1, 0, 7, INF, 2],
    [INF, INF, 7, 0, 2, 3],
    [INF, INF, INF, 2, 0, 1],
    [7, INF, 2, 3, 1, 0]
]

shortest_paths = floyd_warshall(graph)

for row in shortest_paths:
    print(row)
