def alibaba(q, arr):
    m = []
    res = []

    drr = {int(i): arr.count(i) for i in arr}

    while q > 0:
      s = input().split()

      if s[0] == '1':

        b = list(map(int, input().split()))
        nums_b = {int(i): b.count(i) for i in b}
        
        m.append(nums_b)


      elif s[0] == '2':
        counter = 0
        l, r = int(s[1]) - 1, int(s[2])
        
        nums_a = {int(i): drr[i] for i in arr[l:r]}
        

        for nums_b in m:
          counter += nums_a == nums_b

        res.append(counter)

      q -= 1
    return res



n, q = list(map(int, input().split()))
arr = list(map(int, input().split()))

res = alibaba(q, arr)
for r in res:
  print(r)