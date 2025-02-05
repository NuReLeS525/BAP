a = 5
b = 7
def sum_without_addition(a, b):
  if b > 0:
    b -= 1
    a += sum_without_addition(1, b)
  return a

print(sum_without_addition(a, b))