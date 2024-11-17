def remove(s):
    count = s.count('.')
    new_string = s.replace('.', '')
    return new_string, count

input_str = input("Введите строку: ")

result, removed = remove(input_str)

print("Строка без точек:", result)
print("Количество удаленных точек:", removed)