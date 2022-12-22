# 23. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

def multiple_pair(lst):
    mult_list = []
    for i in range(len(lst) // 2):
        mult_list.append(lst[i] * lst[-(i + 1)])

    if len(lst) % 2 == 1:
        index_middle_element = len(lst) // 2
        mult_list.append(lst[index_middle_element] ** 2)

    return mult_list


print(multiple_pair([2, 3, 4, 5, 6]))
print(multiple_pair([2, 3, 5, 6]))
print(multiple_pair([2, 3, 12, 10, 7, -1, 0, 5, 6]))
