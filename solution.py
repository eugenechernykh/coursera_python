S, N = list(map(int, input().split()))
a = [int(input()) for i in range(N)]

a.sort()
summa = 0
answer = 0

for i in range(len(a)):
    summa += a[i]
    if summa <= S:
        answer = i + 1
    else:
        break

print(answer)
