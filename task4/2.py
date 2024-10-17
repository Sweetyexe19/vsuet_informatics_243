list = []
a = int(input())
b = int(input())

if a < b:
    for otvet in range(a, b + 1):
        print(otvet, end=' ')
else:
    for otvet in range(a, b - 1, -1):
        print(otvet, end=' ')