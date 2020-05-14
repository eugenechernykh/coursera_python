x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if (x1 + y1 + x2 + y2) % 2 == 0 and y2-y1 > 0 and y2-y1 >= abs(x2-x1) >= 0:
    print('YES')
else:
    print('NO')
