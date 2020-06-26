"""
https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/53SZY/polighloty
Каждый из N школьников некоторой школы знает Mᵢ языков. Определите, какие языки
знают все школьники и языки, которые знает хотя бы один из школьников.

Формат ввода
Первая строка входных данных содержит количество школьников N. Далее идет N
чисел Mᵢ, после каждого из чисел идет Mᵢ строк, содержащих названия языков,
которые знает i-й школьник. Длина названий языков не превышает 1000 символов,
количество различных языков не более 1000. 1≤N≤1000, 1≤Mᵢ≤500.

Формат вывода
В первой строке выведите количество языков, которые знают все школьники.
Начиная со второй строки - список таких языков. Затем - количество языков,
которые знает хотя бы один школьник, на следующих строках - список таких языков.
"""
n = int(input())
languages, answer = set(), set()
union_lang = list()

while n != 0:
    for i in range(int(input())):
        languages.add(input())
    answer.update(languages)
    union_lang.append(languages)
    languages = set()
    n -= 1

answer1 = answer
for langs in union_lang:
    answer1 &= langs
print(len(answer1))
print(*answer1, sep='\n')

print(len(answer))
print(*answer, sep='\n')
"""
The example of an idea how to process disjunction during the main cycle (if i == 0)
union = set()
all1 = set()
for i in range(int(input())):
    m = int(input())
    a = {input() for j in range(m)}
    all1.update(a)
    if i == 0:
        union.update(a)
    else:
        union &= a
print(len(union))
print('\n'.join(sorted(union)))
print(len(all1))
print('\n'.join(sorted(all1)))
"""