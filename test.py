my_dict = {}
unsorted_list = []
with open('input.txt') as inFile:
    my_list = inFile.read().split()
for word in my_list:
    my_dict[word] = my_dict.get(word, 0) + 1





