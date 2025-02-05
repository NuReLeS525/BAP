
# def tickets(n, a):
#   for coin in range(len(a)):
#     if a[coin] != 25 and a[coin] - sum(a[coin:]) not in a[coin:]:
#       return 'NO'
    
#   return 'YEES++S'

# n = int(input())
a = [int(i) for i in input().split()]

s = 0
for i in a:
  if i == 25:
    s += 25
  elif i == 50:
    if s <= 0:
      print('NO')
      s = False
      break
    s -= 25
  elif i == 75:
    if s <= 0:
      print('NO')
      s = False
      break
    s -= 50
  elif i == 100:
    if s <= 0:
      print('NO')
      s = False
      break
    s -= 75

if s != False:
  print('YES')