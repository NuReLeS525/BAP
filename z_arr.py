a = [i for i in range(int(input()))]
print(a)
print('Please, write an index you want to change')
index = input()
comma = index.find(',')
dec = index[0:comma]

print(dec)
one = index[comma+1:len(index)]
print(one)

# for i in range(len(a)):
