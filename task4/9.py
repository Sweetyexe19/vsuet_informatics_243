n = int(input())
a, b, summa = 0, 1, 0

for i in range(n):
    summa += a
    a, b = b, a + b
print(summa)
