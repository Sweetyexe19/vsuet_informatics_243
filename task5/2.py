def delitel(n):
    for i in range(2, n+1):
        if n % i == 0:
            return i

num = int(input())
if num >= 2:
    print(delitel(num))
else:
    print('error')