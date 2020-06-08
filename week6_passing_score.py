'''
https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/9FHfN/prokhodnoi-ball
Для поступления в вуз абитуриент должен предъявить результаты трех экзаменов в
виде ЕГЭ, каждый из них оценивается целым числом от 0 до 100 баллов. При этом
абитуриенты, набравшие менее 40 баллов (неудовлетворительную оценку) по любому
экзамену из конкурса выбывают. Остальные абитуриенты участвуют в конкурсе по
сумме баллов за три экзамена.

В конкурсе участвует N человек, при этом количество мест равно K. Определите
проходной балл, то есть такое количество баллов, что количество участников,
набравших столько или больше баллов не превосходит K, а при добавлении к ним
абитуриентов, набравших наибольшее количество баллов среди непринятых
абитуриентов, общее число принятых абитуриентов станет больше K.
'''
with open('input.txt', 'r', encoding='utf8') as inFile, \
        open('output.txt', 'w', encoding='utf8') as outFile:

    def passing_score(A, K):
        # function which returns answer in accordance with conditions
        if len(A) <= K:
            return 0
        count_list = [0] * 301
        answer = []
        summa = 0
        # counting sort returns descending lists as (non-zero sum, index)
        for item in A:
            count_list[item] += 1
        for i in range(len(count_list) - 1, -1, -1):
            if count_list[i] != 0:
                answer.append((i, count_list[i]))
        # checking the condition
        for i in range(len(answer)):
            summa += answer[i][1]
            if summa > K and summa == answer[0][1]:
                return 1
            elif summa > K:
                return answer[i - 1][0]

    my_list = []
    for line in inFile:
        my_list.append(line.split())
    # parsing the file in accordance with conditions
    K = int(my_list[0][0])
    data = []
    for i in range(1, len(my_list)):
        if int(my_list[i][-1]) >= 40 and int(my_list[i][-2]) >= 40 and \
                int(my_list[i][-3]) >= 40:
            data.append(
                int(my_list[i][-1]) + int(my_list[i][-2]) + int(
                    my_list[i][-3]))
    data.sort(reverse=True)

    print(passing_score(data, K),file=outFile)
