m = 5000
p = 0.05

y = 3
s = 0


# for i in range(1, y+1):
#   m += m * p
#   print(m)

def bank(m, p, y):
  if y > 0:
    return bank(m + m * p, p, y - 1)
  return m
  
print(bank(m, p, y))