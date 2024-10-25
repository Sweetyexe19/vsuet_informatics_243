c = 0
pre = None

while True:
    number = int(input("Введите натуральное число 0 для завершения: "))

    if number == 0:
        break

    if pre is not None and number > pre:
        c += 1

    previous_number = number
print(c)
