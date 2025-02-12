n = int(input("How many vertices we'll add: "))
graph = {}
for i in range(4 + n):
    graph[i + 1] = set()
# Connect new vertices into a complete subgraph
for i in range(5, 5 + n):
    for j in range(5, 5 + n):
        if j != i:
            graph[i].add(j)
            graph[j].add(i)

def connectconsts(cur):
    # Get original vertices and their degrees
    original = [x for x in graph if x <= 4]
    lengths = [len(graph[x]) for x in original]
    min_deg = min(lengths)
    # Find original vertices with min degree excluding current
    candidates = [x for idx, x in enumerate(original) if lengths[idx] == min_deg and x != cur]
    if not candidates:
        # If all others are the same or higher, pick any other original vertex
        candidates = [x for x in original if x != cur]
    selected = candidates[0]
    graph[cur].add(selected)
    graph[selected].add(cur)

# Ensure each original vertex has at least 2 edges
for i in range(1, 5):
    while len(graph[i]) < 2:
        # Try to connect to new vertices first
        new_vertices = [x for x in graph if x > 4]
        if new_vertices:
            # Find new vertices with the smallest degree
            degrees = [len(graph[x]) for x in new_vertices]
            min_deg = min(degrees)
            candidates = [x for idx, x in enumerate(new_vertices) if degrees[idx] == min_deg]
            # Avoid connecting to the same vertex multiple times
            for candidate in candidates:
                if candidate not in graph[i]:
                    graph[i].add(candidate)
                    graph[candidate].add(i)
                    break
            else:
                # All candidates already connected, fall back to connectconsts
                connectconsts(i)
        else:
            # No new vertices, use connectconsts
            connectconsts(i)

for vertex in graph:
    print(f"{vertex}: {sorted(graph[vertex])}")
