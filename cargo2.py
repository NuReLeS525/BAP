def create_graph(n):
    graph = {i: set() for i in range(1, 5 + n)}

    for i in range(1, 4):
        graph[i].add(i + 1)
        graph[i + 1].add(i)
    graph[4].add(1)
    graph[1].add(4)

    # Создание полного подграфа для новых вершин (начиная с 5)
    for i in range(5, 5 + n):
        for j in range(5, 5 + n):
            if i != j:
                graph[i].add(j)
                graph[j].add(i)

    # Связывание исходных 4 вершин с новыми вершинами
    # Каждая исходная вершина должна иметь степень 2
    # Уже есть одна связь в цикле, добавляем ещё одну связь с новой вершиной
    for i in range(1, 5):
        # Находим новую вершину с минимальной степенью
        min_degree_vertex = min(range(5, 5 + n), key=lambda x: len(graph[x]))
        graph[i].add(min_degree_vertex)
        graph[min_degree_vertex].add(i)

    return graph

# Ввод количества вершин
n = int(input("Введите количество новых вершин: "))
if n < 0:
    print("Количество вершин не может быть отрицательным.")
else:
    graph = create_graph(n)
    for vertex, neighbors in graph.items():
        print(f"{vertex}: {sorted(neighbors)}")
