# 27. Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число.
# В качестве символа-разделителя используйте пробел.
# 12 34 4 456 432
from random import randint

num_list = [str(randint(1, 999)) for _ in range(randint(2, 10))]
print(num_list)
string = ' '.join(num_list)

# string = input('Введите числа: ')
numbers = list(map(int, string.split()))
print(f'max: {max(numbers)}   min: {min(numbers)}')
