'''
Дана последовательность целых чисел, заканчивающаяся числом 0.
Выведите эту последовательность в обратном порядке.
При решении этой задачи нельзя пользоваться массивами и прочими динамическими структурами данных.Рекурсия вам поможет.
'''
def reverse():
    n = int(input())
    if n != 0:
        reverse()
        print(n)
    else:
        print(0)


reverse()
