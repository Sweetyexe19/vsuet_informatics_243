def print_odd_positioned_numbers(count=1):
    number = int(input())

    if number == 0:
        return
    if count % 2 != 0:
        print(number)

    print_odd_positioned_numbers(count + 1)

print_odd_positioned_numbers()