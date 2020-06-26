'''
https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/iw02h/tieliefonnyie-nomiera
Телефонные номера в адресной книге мобильного телефона имеют один из следующих форматов:
+7<код><номер>
8<код><номер>
<номер>
где <номер> — это семь цифр, а <код> — это три цифры или три цифры в круглых скобках.
Если код не указан, то считается, что он равен 495. Кроме того, в записи телефонного
номера может стоять знак “-” между любыми двумя цифрами (см. пример). На данный момент
в адресной книге телефона Васи записано всего три телефонных номера, и он хочет записать
туда еще один. Но он не может понять, не записан ли уже такой номер в телефонной книге.
Помогите ему! Два телефонных номера совпадают, если у них равны коды и равны номера.
Например, +7(916)0123456 и 89160123456 — это один и тот же номер.

Формат ввода

В первой строке входных данных записан номер телефона, который Вася хочет добавить
в адресную книгу своего телефона. В следующих трех строках записаны три номера телефонов,
которые уже находятся в адресной книге телефона Васи. Гарантируется, что каждая из записей
соответствует одному из трех приведенных в условии форматов.

Формат вывода

Для каждого телефонного номера в адресной книге выведите YES, если он совпадает
с тем телефонным номером,который Вася хочет добавить в адресную книгу или NO в противном случае.
'''


def format_number(phone):
    # Returns formatted number in accordance with the list of forbidden signs
    for sign in tuple('(-)+'):
        phone = phone.replace(sign, '')
    if len(phone) < 11:
        phone = '7495' + phone
    phone = phone[1:]
    return phone


def digitizer(phone):
    # Returns the number as a string with digits only
    temp_string = ''
    for n in phone:
        if n.isdigit():
            temp_string += n
    if len(temp_string) < 11:
        temp_string = '7495' + temp_string
    phone = temp_string[1:]
    return phone


# phones = [format_number(input()) for i in range(4)]
phones = [digitizer(input()) for i in range(4)]
for phone_number in phones[1:]:
    print('YES' if phone_number == phones[0] else 'NO')
