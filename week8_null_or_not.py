'''
https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/9uqay/nol-ili-nie-nol
Проверьте, есть ли среди данных N чисел нули.
Формат ввода
Вводится число N, а затем N чисел.
Формат вывода
Выведите True, если среди введенных чисел есть хотя бы один нуль, или False в
противном случае.
'''
print(
      any(
          map(
              lambda x: x == 0,
              map(
                  lambda x: int(input()),
                  range(int(input()))
                 )
              )
         )
)
