# 24. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random

count = int(input('\nЗадайте размерность списка: '))
# Создаем список вещественных чисел:
num_list = []
for _ in range(count):
    new_num = round(random.random() * random.choice([1, 10, 100, 1000]), 2)
    num_list.append(new_num)

print(num_list)


# VAR_#1 --------------------------------
# Создаем список дробных частей:
fract_part_list = [i - int(i) for i in num_list]

# Удаляем из списока дробных частей все нулевые элементы:
for _ in range(len(fract_part_list)):
    for elem in fract_part_list:
        if elem == 0:
            fract_part_list.remove(elem)

diff = round(max(fract_part_list) - min(fract_part_list), 4)
print('var_1:', diff)


# VAR_#2 --------------------------------
def diff_fract_part(lst):
    max_el = 0
    min_el = 1

    for elem in lst:
        fract_part = elem - int(elem)
        if fract_part != 0 and (fract_part > max_el):
            max_el = fract_part
        if fract_part != 0 and (fract_part < min_el):
            min_el = fract_part

    return round(max_el - min_el, 4)


print('var_2:', diff_fract_part(num_list))
