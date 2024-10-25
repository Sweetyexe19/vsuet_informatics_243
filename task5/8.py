maxn = 0
c = 1
pre = None

while True:
    number = int(input("Введите натуральное число 0 для завершения "))

    if number == 0:
        break

    if pre is not None:
        if number == pre:
            c += 1
        else:
            maxn = max(maxn, c)
            c = 1

    pre = number
max_count = max(maxn, c)

print(maxn)
