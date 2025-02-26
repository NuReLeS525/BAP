INF = float('inf')

def floyd_warshall_with_tracking(graph):
    n = len(graph)
    
    dist = [row[:] for row in graph]
    next_node = [[None if graph[i][j] == INF else j for j in range(n)] for i in range(n)]
    
    all_paths = []

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    next_node[i][j] = next_node[i][k]

        current_paths = [[None if dist[i][j] == INF else reconstruct_path(i, j, next_node) 
                          for j in range(n)] for i in range(n)]
        all_paths.append(current_paths)

    return dist, next_node, all_paths

def reconstruct_path(start, end, next_node):
    path = []
    if next_node[start][end] is None:
        return path
    while start != end:
        path.append(start)
        start = next_node[start][end]
    path.append(end)
    return path

def print_all_paths_during_algorithm(graph):
    shortest_paths, next_node, all_paths = floyd_warshall_with_tracking(graph)

    for step, paths in enumerate(all_paths):
        print(f"\nIteration {step + 1}:")
        for i in range(len(graph)):
            for j in range(len(graph)):
                if shortest_paths[i][j] == INF:
                    print(f"Shortest path from {i} to {j}: No path")
                else:
                    path = paths[i][j]
                    print(f"Shortest path from {i} to {j}: {path} with distance {shortest_paths[i][j]}")

graph = [
    [0, 3, INF, INF, INF, 7],
    [3, 0, 1, INF, INF, INF],
    [INF, 1, 0, 7, INF, 2],
    [INF, INF, 7, 0, 2, 3],
    [INF, INF, INF, 2, 0, 1],
    [7, INF, 2, 3, 1, 0]
]

print_all_paths_during_algorithm(graph)
