a = int(input())
b = int(input())
c = int(input())
p = (a+b+c)/2
s = p*(p-a)*(p-b)*(p-c)
maxSide = max(a, b, c)
if not s > 0:
    print('impossible')
elif maxSide == c:
    cond = a**2 + b**2
    if maxSide**2 > cond:
        print('obtuse')
    elif maxSide**2 < cond:
        print('acute')
    else:
        print('rectangular')
elif maxSide == b:
    cond = a**2 + c**2
    if maxSide**2 > cond:
        print('obtuse')
    elif maxSide**2 < cond:
        print('acute')
    else:
        print('rectangular')
elif maxSide == a:
    cond = c**2 + b**2
    if maxSide**2 > cond:
        print('obtuse')
    elif maxSide**2 < cond:
        print('acute')
    else:
        print('rectangular')
a = float(input())
b = float(input())
c = float(input())
p = (a+b+c)/2
s = (p*(p-a)*(p-b)*(p-c))**0.5
if int(s) == s:
    print(int(s))
else:
    print('{0:.6f}'.format(s))

from math import floor, ceil, sqrt
x = int(input())
n = 1
summa = 0
kvadrat = 0
while x != 0:
        summa += x
        kvadrat += x**2
        x = int(input())
        n += 1
n = n - 1
s = summa/n
chislitel = (kvadrat + s*(s*n-2*summa))
sigma = sqrt(chislitel/(n-1))
print('{0:.11f}'.format(sigma))

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())


def length(a, b, c, d):
    return ((c - a) ** 2 + (d - b) ** 2) ** 0.5


p = length(x1, y1, x2, y2) + length(x1, y1, x3, y3) + length(x2, y2, x3, y3)
print('{:.5f}'.format(p))