def main():
  n, m = list(map(int, input().split()))
  # matrix = [[] for _ in range(n)]
  mx = []
  for i in range(n):
    mx.append(input())

  for i in range(n):
    cross = mx[i]
    for j in range(m):
      cross += mx[j][i]
      
    


t = int(input())

for _ in range(t):
  main()

