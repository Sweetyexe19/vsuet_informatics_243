sum = 0
c = 0

while True:
    number = int(input("Введите число 0 для завершения: "))

    if number == 0:
        break

    sum += number
    c += 1

if c > 0:
    avg = sum / c
    print(avg)
else:
    print("Не было введено ни одного числа")
