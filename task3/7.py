god = int(input('Введи год'))

if (god % 4 == 0 and god % 100 != 0) or god % 400 == 0:
    print("Да")
else:
    print("Нет")
