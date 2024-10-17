a = int(input())
b = int(input())

if a < b:
    print('error')
else:
    for otvet in range(a, b - 1,- 1):
        if otvet % 2 == 0:
            print(otvet, end=' ')
