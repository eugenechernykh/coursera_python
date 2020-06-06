def CountSort(A):
    count_list = [0] * 101
    for item in A:
        count_list[item] += 1
    for i in range(len(count_list)):
        print((str(i) + ' ') * count_list[i], end='')


my_list = map(int, input().split())
print(CountSort(my_list))
