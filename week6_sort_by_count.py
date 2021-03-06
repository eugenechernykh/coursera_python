'''
Дан список из N (N≤2*10⁵) элементов, которые принимают целые значения от 0 до 100 (100 включая).
Отсортируйте этот список в порядке неубывания элементов. Выведите полученный список.
Решение оформите в виде функции CountSort(A), которая модифицирует передаваемый ей список.
Использовать встроенные функции сортировки нельзя.
'''
def CountSort(A):
    count_list = [0] * 101
    for item in A:
        count_list[item] += 1
    for i in range(len(count_list)):
        print((str(i) + ' ') * count_list[i], end='')


my_list = map(int, input().split())
CountSort(my_list)
