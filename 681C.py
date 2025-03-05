import sys
import heapq

def fix_operations(n, operations):
    heap = []
    result = []
    
    for op in operations:
        parts = op.split()
        if parts[0] == "insert":
            x = int(parts[1])
            heapq.heappush(heap, x)
            result.append(op)
        elif parts[0] == "getMin":
            x = int(parts[1])
            # Удаляем элементы, пока минимум не станет x
            while heap and heap[0] < x:
                heapq.heappop(heap)
                result.append("removeMin")
            # Если кучи нет или минимум не x, вставляем x
            if not heap or heap[0] > x:
                heapq.heappush(heap, x)
                result.append(f"insert {x}")
            result.append(op)  # Запоминаем getMin
        elif parts[0] == "removeMin":
            if not heap:
                # Если куча пуста, добавляем произвольный элемент
                result.append("insert 0")
                heapq.heappush(heap, 0)
            heapq.heappop(heap)
            result.append(op)
    
    print(len(result))
    print("\n".join(result))

# Читаем входные данные
n = int(sys.stdin.readline().strip())
operations = [sys.stdin.readline().strip() for _ in range(n)]

# Вызываем функцию исправления
fix_operations(n, operations)
