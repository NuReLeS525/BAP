import sys

class DSU:
    """Структура данных для динамического объединения множеств (Union-Find с путевым сжатием)."""
    
    def __init__(self, n):
        self.parent = list(range(n + 1))  # Родитель каждого узла
        self.size = [1] * (n + 1)  # Размер компоненты, по умолчанию 1
    
    def find(self, v):
        """Находит корень множества с сжатием пути."""
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])  # Сжатие пути
        return self.parent[v]

    def union(self, a, b):
        """Объединяет два множества."""
        rootA = self.find(a)
        rootB = self.find(b)
        if rootA != rootB:
            if self.size[rootA] < self.size[rootB]:
                rootA, rootB = rootB, rootA  # Всегда присоединяем меньшую компоненту к большей
            self.parent[rootB] = rootA
            self.size[rootA] += self.size[rootB]

def main():
    # Считываем входные данные
    n, m = map(int, sys.stdin.readline().split())
    
    # Создаём DSU
    dsu = DSU(n)
    print(dsu.parent)
    print(dsu.size)
    
    # Обрабатываем группы
    for _ in range(m):
        group = list(map(int, sys.stdin.readline().split()))
        if group[0] > 1:
            first_user = group[1]
            for user in group[2:]:
                dsu.union(first_user, user)  # Объединяем пользователей в одной группе
    
    # Вычисляем размер каждой компоненты
    result = [0] * (n + 1)
    for user in range(1, n + 1):
        root = dsu.find(user)
        result[user] = dsu.size[root]
    
    # Вывод ответа
    print(*result[1:])

if __name__ == "__main__":
    sys.setrecursionlimit(10**6)  # Увеличиваем лимит рекурсии для DSU
    main()
