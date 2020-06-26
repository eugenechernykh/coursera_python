'''
https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/4JHKe/chastotnyi-analiz/discussions
Дан текст. Выведите все слова, встречающиеся в тексте, по одному на каждую строку.
Слова должны быть отсортированы по убыванию их количества появления в тексте,
а при одинаковой частоте появления — в лексикографическом порядке.

Указание.

После того, как вы создадите словарь всех слов, вам захочется отсортировать его
по частоте встречаемости слова. Желаемого можно добиться, если создать список,
элементами которого будут кортежи из двух элементов: частота встречаемости
слова и само слово. Например, [(2, 'hi'), (1, 'what'), (3, 'is')]. Тогда
стандартная сортировка будет сортировать список кортежей, при этом кортежи
сравниваются по первому элементу, а если они равны —то по второму. Это почти
то, что требуется в задаче.
'''
my_dict = {}
with open('input.txt') as inFile:
    my_list = inFile.read().split()
for word in my_list:
    my_dict[word] = my_dict.get(word, 0) + 1
for item in sorted(my_dict.items(), key=lambda x: (-x[1], x[0])):
    print(item[0])
# Тоже самое только через сам словарь
#print(*sorted(sorted(my_dict), key=lambda x: my_dict[x], reverse=True), sep='\n')