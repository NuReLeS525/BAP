def euclid(n, m):
  if m == 0:
    return n
  return euclid(m, n%m)

def semi_prime(n):
  

def main(a):
  count = 0
  i, j = 0, 0
  nok = int(i * j / euclid(i, j))
  while i < len(a):

    if semi_prime(nok):
      count += 1
  return count



t = int(input())

for _ in range(t):
  n = int(input())
  a = list(map(int, input().split()))

  a_count = main(a)
  ans = []
  ans.append(a_count)

for el in ans:
  print(el)