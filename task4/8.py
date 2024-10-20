n = int(input())

for i in range(1, n + 1):
    print(''.join(str(z) for z in range(1, i + 1)))
