n, m = input().split()
n, m = int(n), int(m)
r = int(input())

# n == r or m == r

# n % r != 0 or m % r != 0

# there may be placed few circles inside the box or not
w = 0
h = 0
counter = h * w
if n % r == 0:
  h = (n // r)
else:
  