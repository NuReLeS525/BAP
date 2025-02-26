def min_change(n, s):
    left = -1
    right = -1
    
    for i in range(n):
        if s[i] == '1' and left == -1:
            left = i
        if s[i] == '0':
            right = i
    
    if left == -1 or right == -1 or left > right:
        return 0
    
    return right - left + 1

t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    s = input().strip()
    print(min_change(n, s))
