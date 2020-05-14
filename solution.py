n = int(input())
m = int(input())


def ReduceFraction(n, m):
    if n == m:
        return 1, 1
    if n > m:
        for i in range(2, m + 1):
            if n % i == 0 and m % i == 0:
                n, m = ReduceFraction(n // i, m // i)
                return n, m
    if n < m:
        for i in range(2, n + 1):
            if n % i == 0 and m % i == 0:
                n, m = ReduceFraction(n // i, m // i)
                return n, m
    return n, m


print(*ReduceFraction(n, m))
