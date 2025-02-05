import math
a = []
t = int(input())
for i in range(t):
  x, y, d = [int(i) for i in input().split()]
  result = x / d + math.ceil(abs(y - x) / d + int(y / d))
  if x < y:
    result += 1
  elif x > y:
    result -= 1
  a.append(result)

for el in a:
  print(el)