sutki = 1440
n = int(input("Введите число:"))
if n > sutki:
    print('Nevalid')
else:
    hours = n % (60 * 24) // 60
    minutes = n % 60
    print(hours, minutes)