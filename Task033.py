# 33. Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена
# и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
from random import randint


def create_polynomial(degree, max_ratio):
    random_list = [randint(0, max_ratio) for i in range(degree + 1)]

    dict = {}
    for i in range(degree, -1, -1):
        dict[i] = random_list[i]
    print(dict)

    string = ''
    for key, val in dict.items():
        if val == 0:
            continue
        if key == 0:
            string += str(val) + ' + '
        if key == 1 and val == 1:
            string += 'x + '
        if key == 1 and val > 1:
            string += str(val) + '*x + '
        if val == 1 and key > 1:
            string += 'x**' + str(key) + ' + '
        if val > 1 and key > 1:
            string += str(val) + '*x**' + str(key) + ' + '
    string = string[:-3] + ' = 0'

    return string


degree = int(input('Введите степень многочлена: '))
m = 100

polynomial = create_polynomial(degree, m)

with open('Task033.txt', 'w', encoding='utf-8') as file:
    file.write(polynomial + '\n')

# Первый файл для 35-й задачи:
# with open('Task035-1.txt', 'w', encoding='utf-8') as file:
#     file.write(polynomial + '\n')
#
# Второй файл для 35-й задачи:
# with open('Task035-2.txt', 'w', encoding='utf-8') as file:
#     file.write(polynomial + '\n')
