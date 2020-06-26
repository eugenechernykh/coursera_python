'''
https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/FdeT5/vybory-priezidienta
В выборах Президента Российской Федерации побеждает кандидат, набравший свыше
половины числа голосов избирателей. Если такого кандидата нет, то во второй тур
выборов выходят два кандидата, набравших наибольшее число голосов.

Формат ввода

Каждая строка входного файла содержит имя кандидата, за которого отдал голос
один избиратель. Известно, что общее число кандидатов не превосходит 20, но в
отличии от предыдущих задач список кандидатов явно не задан. Читайте данные из
файла input.txt с указанием кодировки utf8.

Формат вывода

Если есть кандидат, набравший более 50% голосов, программа должна вывести его
имя. Если такого кандидата нет, программа должна вывести имя кандидата,
занявшего первое место, затем имя кандидата, занявшего второе место. Выводите
данные в файл output.txt с указанием кодировки utf8.
'''
my_dict = {}
with open('input.txt', 'r', encoding='utf8') as inFile, \
        open('output.txt', 'w', encoding='utf8') as outFile:
    my_list = inFile.read().splitlines()
    for word in my_list:
        my_dict[word] = my_dict.get(word, 0) + 1
    max_value = max(my_dict.values())
    if max_value > len(my_list) / 2:
        for key, value in my_dict.items():
            if value is max_value:
                print(key, file=outFile)
    else:
        for i in range(2):
            print(
                sorted(sorted(my_dict), key=lambda x: my_dict[x],
                       reverse=True)[i],
                file=outFile)
