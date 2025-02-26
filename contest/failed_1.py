def sol(s):
  res = 0
  if '0' not in s:
    return 1
  elif '1' not in s:
    return 0
  elif s[-1] == '1':
    res = 1

  res += s.count('10') * 2
  return res

t = int(input())
answer = ''
for i in range(t):
  n = int(input())
  s = input()
  answer += str(sol(s)) + '\n'

print(answer)