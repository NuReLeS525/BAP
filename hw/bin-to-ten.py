from math import log2

def DecimalToBinary(num):
    if num >= 1:
        DecimalToBinary(num // 2)
    print(num % 2, end = '')



def dec_bin(n):
    length = int(log2(n)) + 1
    num = [0] * length
    num[0] = 1
    while n > 1:
        print(log2(n))
        num[-1-int(log2(n))] = 1
        n -= 2**int(log2(n))
    if n == 1:
        num[-1] = 1
    return num

def bin_dec(n):
    num = str(n)[::-1]
    ans = 0
    for i in range(len(num)):
        if int(num[i]) == 1:
            ans += 2**i
    return ans
DecimalToBinary(1234)
print('')
print(bin_dec(1010))