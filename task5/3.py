def ratata(n):
    step = 1
    while step *2 <= n:
        step *= 2
    return step

n = int(input())
otvet = ratata(n)
print(otvet)