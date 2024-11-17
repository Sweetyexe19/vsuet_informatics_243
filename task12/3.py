def reverse_number(n):
    if n < 0:
        print('-', end='')
        n = -n

    num_str = str(n)

    def recursive_print(index):
        if index < 0:
            return
        print(num_str[index], end='')
        recursive_print(index - 1)

    recursive_print(len(num_str) - 1)
    print()

reverse_number(12345) #вывод 54321
