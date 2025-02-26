import sys
from collections import defaultdict

def main():
    sys.setrecursionlimit(1 << 25)
    n = int(sys.stdin.readline())
    if n % 2 != 0:
        print(-1)
        return
    
    graph = defaultdict(list)
    for _ in range(n-1):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)
    
    count = 0
    
    def dfs(u, parent):
        nonlocal count
        size = 1
        for v in graph[u]:
            if v != parent:
                size += dfs(v, u)
        if size % 2 == 0:
            count += 1
            size = 0
        return size
    
    dfs(1, -1)
    print(count - 1)

if __name__ == "__main__":
    main()
