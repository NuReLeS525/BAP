n = int(input())
x = int(input())
power = n*x
print(power)
if power / 4 % 1 == 0.0:
    print(6)
elif power / 4 % 1 == 0.25:
    print(2)
elif power / 4 % 1 == 0.5:
    print(4)
elif power / 4 % 1 == 0.75:
    print(8)
# for i in range(1, 15):
#     print(i / 4 % 1)
#     print(i, 2 ** i)
#     print('=============')