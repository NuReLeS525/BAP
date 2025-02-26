def regular(row):
  if len(row) == 1:
    return False

  if len(row) % 2 != 0:
    del row[-1]
  
  print(row)
  index_of_row = sum(row)
  print(row[0], index_of_row)
  row[0] = row[0] - abs(index_of_row)
  print(row)



# n = int(input())
a = [int(i) for i in input().split()]

regular(a)