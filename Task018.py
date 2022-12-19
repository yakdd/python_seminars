# 18. Реализуйте алгоритм перемешивания списка.

from random import randint as rnd


ini_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd']
print(ini_list)

for i in range(len(ini_list)):
    elem = ini_list.pop(rnd(0, len(ini_list) - 1))
    ini_list.insert(rnd(0, len(ini_list) - 1), elem)

print(ini_list)
