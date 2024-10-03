n = int(input("Кол-во строк: "))
m = int(input("Кол-во столбцов: "))
k = int(input("Кол-во долек: "))

if k <= n * m and (k % n == 0 or k % m == 0):
    print("Да")
else:
    print("Нет")
