def factorial(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res


n = int(input())

for i in range(1, n):
    sum += factorial(i)
print(sum)
