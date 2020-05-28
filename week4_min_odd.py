'''
Выведите значение наименьшего нечетного элемента списка, гарантируется, что хотя бы один нечётный элемент в списке есть.

3 решения с таймингами
'''
import time as t

# print('123 '*10000)
intList = list(map(int, input().split()))

# first solution
tic = t.time()


def isOdd(a):
    for i in range(len(a)):
        if a[i] % 2 == 1:
            count = a[i]
            return count, i
    return


odd, index = isOdd(intList)

for i in range(index + 1, len(intList)):
    if intList[i] % 2 == 1 and intList[i] < odd:
        odd = intList[i]
toc = t.time()
print(odd)
print('{:15f}'.format(toc - tic))

# second solution
tic1 = t.time()
oddy = list()
for i in range(len(intList)):
    if intList[i] % 2 == 1:
        oddy.append(intList[i])
toc1 = t.time()
print(min(oddy))
print('{:15f}'.format(toc1 - tic1))

# third solution
tic2 = t.time()
aa = min(int(i) for i in intList if int(i) % 2 != 0)
toc2 = t.time()
print(aa)
print('{:15f}'.format(toc2 - tic2))
