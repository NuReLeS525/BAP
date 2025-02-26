import sys

def is_valid_rearrangement(n, a):
    visited = set()
    
    for k in range(n):
        new_room = (k + a[k] % n + n) % n
        if new_room in visited:
            return "NO"
        visited.add(new_room)
    
    return "YES"

def main():
    t = int(input().strip())
    results = []
    
    for _ in range(t):
        n = int(input().strip())
        a = list(map(int, input().strip().split()))
        results.append(is_valid_rearrangement(n, a))
    
    print("\n".join(results))

if __name__ == "__main__":
    main()