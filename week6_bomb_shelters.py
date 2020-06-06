'''
Штаб гражданской обороны Тридесятой области решил обновить план спасения на случай ядерной атаки. Известно, что все n
селений Тридесятой области находятся вдоль одной прямой дороги. Вдоль дороги также расположены m бомбоубежищ, в которых
жители селений могут укрыться на случай ядерной атаки.
Чтобы спасение в случае ядерной тревоги проходило как можно эффективнее, необходимо для каждого селения определить
ближайшее к нему бомбоубежище.
Формат ввода
В первой строке вводится число n - количество селений (1 <= n <= 100000). Вторая строка содержит n различных целых
чисел, i-е из этих чисел задает расстояние от начала дороги до i-го селения. В третьей строке входных данных задается
число m - количество бомбоубежищ (1 <= m <= 100000). Четвертая строка содержит m различных целых чисел, i-е из этих
чисел задает расстояние от начала дороги до i-го бомбоубежища. Все расстояния положительны и не превышают 10⁹. Селение
и убежище могут располагаться в одной точке.
Формат вывода
Выведите n чисел - для каждого селения выведите номер ближайшего к нему бомбоубежища. Бомбоубежища пронумерованы
от 1 до m в том порядке, в котором они заданы во входных данных.
Указание
Создайте список кортежей из пар (позиция селения, его номер в исходном списке), а также аналогичный список для
бомбоубежищ. Отсортируйте эти списки.
Перебирайте селения в порядке возрастания.
Для селения ближайшими могут быть два соседних бомбоубежища, среди них надо выбрать ближайшее. При переходе к следующему
селению не обязательно искать ближайшее бомбоубежище с самого начала. Его можно искать начиная с позиции, найденной для
предыдущего города. Аналогично, не нужно искать подходящее бомбоубежище до конца списка бомбоубежищ: достаточно найти
самое близкое. Если Вы неэффективно реализуете эту часть, то решение тесты не пройдет.
Для хранения ответа используйте список, где индекс будет номером селения, а по этому индексу будет запоминаться номер
бомбоубежища.
'''
# не проходит тест 6, может потом как-нить разберусь :)

def sort_position(n):
    # input data as a tuple with distance and index and sort it out
    tempData = list(map(int, input().split()))
    mylist = []
    for i in range(n):
        manData = (tempData[i], i)
        mylist.append(manData)
    mylist.sort()
    return mylist


def checker(villageList, shelterList):
    # finding nearest shelters before and after the village and comparing the distance to find the closest one
    answer = []
    i = 0
    j = 0
    s_distance_j, shelter_j = shelterList[0]
    while i < len(villageList) and j < len(shelterList):
        v_distance, village = villageList[i]
        s_distance, shelter = shelterList[j]
        if v_distance > s_distance:
            s_distance_j, shelter_j = shelterList[j]
            j += 1
        else:
            diff = abs(v_distance - s_distance)
            diff_j = abs(v_distance - s_distance_j)
            if diff < diff_j:
                answer.append((village + 1, shelter + 1))
            else:
                answer.append((village + 1, shelter_j + 1))
            i += 1
    # filling the answer with the last found shelter if shelters > villages
    for remain_part in range(i, len(villageList)):
        answer.append((i + 1, shelter_j + 1))
    answer.sort()
    return answer


def formatting(mylist):
    for item in mylist:
        print(item[1], end=' ')


n = int(input())
villageList = sort_position(n)
m = int(input())
shelterList = sort_position(m)

formatting(checker(villageList, shelterList))

''' The version which worked out

amount_towns = int(input())
towns = list(enumerate(map(int, input().split()[:amount_towns]), 1))
amount_shelters = int(input())
shelters = list(enumerate(map(int, input().split()[:amount_shelters]), 1))
towns.sort(key=lambda k: k[1])
shelters.sort(key=lambda k: k[1])

index = 0
result = []

for town in towns:
    while (index + 1 < amount_shelters and 
           abs(town[1] - shelters[index][1]) > abs(
            town[1] - shelters[index + 1][1])):
        index += 1
    else:
        result.append([town[0], shelters[index][0]])

result.sort()
for i in result:
    print(i[1], end=' ')
'''
