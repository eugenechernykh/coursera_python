'''
https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/gc73D/samoie-chastoie-slovo
Дан текст. Выведите слово, которое в этом тексте встречается чаще всего.
Если таких слов несколько, выведите то, которое меньше в лексикографическом порядке.
'''
my_dict = {}
with open('input.txt') as inFile:
    my_list = inFile.read().split()
for word in my_list:
    my_dict[word] = my_dict.get(word, 0) + 1
print(max(sorted(my_dict), key=my_dict.get))
