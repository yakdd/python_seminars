# 35. Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

def create_dict_degree_ratio(lst):
    poly_dict = {}
    count = len(lst)

    for _ in range(count):
        for item in lst:
            if '*x**' in item:
                numbers = item.split('*x**')
                poly_dict[int(numbers[1])] = int(numbers[0])
                lst.remove(item)

    for _ in range(count):
        for item in lst:
            if 'x**' in item:
                new_item = item.replace('x**', '')
                poly_dict[int(new_item)] = 1
                lst.remove(item)

    for _ in range(count):
        for item in lst:
            if '*x' in item:
                new_item = item.replace('*x', '')
                poly_dict[1] = int(new_item)

    for item in lst:
        if item == 'x':
            poly_dict[1] = 1
        if item.isdigit():
            poly_dict[0] = int(item)

    return poly_dict


with open('Task035-1.txt', 'r', encoding='utf-8') as file:
    str_1 = file.readline()
with open('Task035-2.txt', 'r', encoding='utf-8') as file:
    str_2 = file.readline()


# Формируем словари "степень: коэффициент" из строк внешних файлов:
list_1 = str_1[:-5].split(' + ')
list_2 = str_2[:-5].split(' + ')

if len(str_1) >= len(str_2):
    first_dict = create_dict_degree_ratio(list_1)
    second_dict = create_dict_degree_ratio(list_2)
else:
    first_dict = create_dict_degree_ratio(list_2)
    second_dict = create_dict_degree_ratio(list_1)
print(first_dict)
print(second_dict)


# Объединяем словари и записываем сумму значений у повторяющихся ключей:
new_dict = {**first_dict, **second_dict}
for k in second_dict.keys():
    if k in first_dict.keys():
        new_dict[k] = first_dict[k] + second_dict[k]


# Составляем упорядоченный многочлен из ключей и значений объединенного словаря:
keys_sorted = [int(i) for i in list(new_dict.keys())]
keys_sorted.sort(reverse=True)

polynomial = ''
for i in keys_sorted:
    if i > 1 and new_dict[i] > 1:
        polynomial += str(new_dict[i]) + '*x**' + str(i) + ' + '
    if i == 1 and new_dict[i] == 1:
        polynomial += 'x + '
    if i > 1 and new_dict[i] == 1:
        polynomial += 'x**' + str(i) + ' + '
    if new_dict[i] == 0:
        continue
    if i == 0 and new_dict[i] > 1:
        polynomial += str(new_dict[i]) + ' + '
    if i == 1 and new_dict[i] > 1:
        polynomial += str(new_dict[i]) + '*x' + ' + '
polynomial = polynomial[:-3] + ' = 0'
print(polynomial)


with open('Task035.txt', 'w', encoding='utf-8') as file:
    file.write(polynomial)
