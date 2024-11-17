def sum_odd(array):
    sum_odd_ = sum(array[i] for i in range(1, len(array), 2))
    return sum_odd_

n = int(input("Введите длину массива: "))

D = []
print("Введите элементы массива:")
for _ in range(n):
    element = float(input())
    D.append(element)

result_sum = sum_odd(D)

print("Массив D:", D)
print("Сумма элементов с нечетными индексами:", result_sum)