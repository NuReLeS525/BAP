import sys
import heapq
from collections import defaultdict

def max_capacity_path(graph, start, end):
    """Находит путь с максимальной пропускной способностью между start и end"""

    # Очередь с приоритетами (max-heap), храним (-вес, вершина)
    pq = [(-float('inf'), start)]  # Начинаем с бесконечного веса
    max_weight = {city: 0 for city in graph}  # Максимальный вес до каждого города
    max_weight[start] = float('inf')  # Для старта веса нет (∞)

    while pq:
        curr_weight, u = heapq.heappop(pq)
        curr_weight = -curr_weight  # Преобразуем обратно в положительный

        # Если дошли до конечного города — возвращаем результат
        if u == end:
            return curr_weight

        # Обрабатываем соседей
        for v, weight in graph[u]:
            # Берём минимальный вес по пути (ограничение дороги)
            new_weight = min(curr_weight, weight)

            # Если нашли больший минимальный вес по пути, обновляем
            if new_weight > max_weight[v]:
                max_weight[v] = new_weight
                heapq.heappush(pq, (-new_weight, v))  # Вставляем в кучу (минус для max-heap)

    return -1  # Если пути нет

# Читаем входные данные
n, m = map(int,
