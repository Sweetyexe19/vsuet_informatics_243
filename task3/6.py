stolb1 = int(input("Введите номер столбца: "))
strok1 = int(input("Введите номер строки: "))

stolb2 = int(input("Введите номер столбца: "))
strok2 = int(input("Введите номер строки: "))

if (stolb1 + strok1) % 2 == (stolb2 + strok2) % 2:
    print("Да")
else:
    print("Нет")
