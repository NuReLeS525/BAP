f = [234, 82, 11, -5, 99, 11, 342, 838, 52]
f = [1, 2, 3, 4, 5, 6]
l = len(f)
w = 3
s = 0 #start f[s]     sum(f[s:e]) 
e = w #end f[e]
min_sum = sum(f)
while e <= l:
  print(f[s:e])
  print(sum(f[s:e]))
  if sum(f[s:e]) < min_sum:
    min_sum = sum(f[s:e])
  s += 1
  e += 1
print(min_sum)

