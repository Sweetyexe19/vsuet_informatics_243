x = int(input())
y = int(input())

day = 1
distant = x

while distant < y:
    day += 1
    distant *= 1.1

print(day)